from VirtualCopernicusNG import TkCircuit
from personal_config import personal_config

configuration = {
    "name": "CopernicusNG Weather Forecast",
    "sheet": "sheet_forecast.png",
    "width": 343,
    "height": 267,

    "servos": [
        {"x": 170, "y": 150, "length": 90, "name": "Servo 1", "pin": 17}
    ],
    "buttons": [
        {"x": 295, "y": 200, "name": "Button 1", "pin": 11},
        {"x": 295, "y": 170, "name": "Button 2", "pin": 12},
    ]
}

circuit = TkCircuit(configuration)

topic = personal_config["my_topic"]
device_id = personal_config["my_device"]

pin_map = {}


@circuit.run
def main():
    from gpiozero import DigitalInputDevice, DigitalOutputDevice, AngularServo
    import json
    import paho.mqtt.client as mqtt

    def init_cmd(client, userdata, msg):
        payload = json.loads(msg.payload)
        print(payload)
        if not payload.keys() >= {"pins"}:
            print("Error, invalid message")
            return
        for pin_setting in payload["pins"]:
            if not pin_setting.keys() >= {"pin", "type"}:
                print("Error, invalid message")
            else:
                initialize(pin_setting["pin"], pin_setting["type"])

    def output_cmd(client, userdata, msg):
        payload = json.loads(msg.payload)
        print(payload)
        if payload.keys() >= {"pin", "state"} and payload.keys() >= {"pin", "angle"}:
            print("Error, invalid messeeage")
            return
        pin = payload["pin"]
        if pin_map[pin]:
            if type(pin_map[pin]) == AngularServo:
                if "angle" in payload:
                    pin_map[pin].angle = payload["angle"]
            else:
                pin_map[pin].value = payload["state"]
                print("Change state of pin {} to {}".format(pin, payload["state"]))

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        mqttc.subscribe(f'{topic}/{device_id}/#')
        mqttc.message_callback_add(f'{topic}/{device_id}/init', init_cmd)
        mqttc.message_callback_add(f'{topic}/{device_id}/output', output_cmd)

    def initialize(pin, device_type):
        if device_type == "DigitalInput":
            device = DigitalInputDevice(pin)
            device.when_activated = lambda: on_action(pin, 0)
            device.when_deactivated = lambda: on_action(pin, 1)
            pin_map[pin] = device
            print("Initialized pin {} as {}".format(pin, device_type))
        elif device_type == "DigitalOutput":
            pin_map[pin] = DigitalOutputDevice(pin)
            print("Initialized pin {} as {}".format(pin, device_type))
        elif device_type == "AngularServo":
            pin_map[pin] = AngularServo(pin)
            print("Initialized pin {} as {}".format(pin, device_type))

    def on_action(pin, state):
        json_var = json.dumps({"pin": pin, "state": state})
        mqttc.publish(f'{topic}/{device_id}/input', json_var, 0, False)

    mqttc = mqtt.Client(personal_config["my_client"])
    mqttc.on_connect = on_connect
    mqttc.connect("test.mosquitto.org", 1883, 60)
    mqttc.loop_forever()