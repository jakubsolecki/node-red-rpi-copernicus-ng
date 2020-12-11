from VirtualCopernicusNG import TkCircuit

configuration = {
    "name": "VirtualCopernicus",
    "sheet": "sheet_smarthouse.png",
    "width": 332,
    "height": 300,
    "leds": [
        {"x": 112, "y": 70, "name": "LED 1", "pin": 21},
        {"x": 71, "y": 141, "name": "LED 2", "pin": 22}
    ],
    "buttons": [
        {"x": 242, "y": 146, "name": "Button 1", "pin": 11},
        {"x": 200, "y": 217, "name": "Button 2", "pin": 12},
    ],
    "buzzers": [
        {"x": 277, "y": 9, "name": "Buzzer", "pin": 16, "frequency": 440},
    ]
}

circuit = TkCircuit(configuration)

topic = "kraleppa/test"
device_id = 1

pin_map = {}


@circuit.run
def main():
    from gpiozero import DigitalInputDevice, DigitalOutputDevice
    import json
    import paho.mqtt.client as mqtt

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        mqttc.subscribe(f'{topic}/{device_id}/input')
        mqttc.subscribe(f'{topic}/{device_id}/init')

    def on_message(client, userdata, msg):
        json_var = json.loads(msg.payload)
        print(json_var)
        if json_var["init"]:
            initialize(json_var["pin"], json_var["type"])
        else:
            pin, state = json_var["pin"], json_var["state"]
            pin_map[pin].value = state

    def initialize(pin, device_type):
        if device_type == "DigitalInput":
            device = DigitalInputDevice(pin)
            device.when_activated = lambda: on_action(pin, 0)
            device.when_deactivated = lambda: on_action(pin, 1)
            pin_map[pin] = device
        elif device_type == "DigitalOutput":
            pin_map[pin] = DigitalOutputDevice(pin)

    def on_action(pin, state):
        json_var = json.dumps({"pin": pin, "state": state})
        mqttc.publish(f'{topic}/{device_id}/output', json_var, 0, False)

    mqttc = mqtt.Client("kraleppa_test")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect

    mqttc.connect("test.mosquitto.org", 1883, 60)

    mqttc.loop_forever()
