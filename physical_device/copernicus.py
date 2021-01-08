from personal_config import personal_config
from threading import Thread


topic = personal_config["my_topic"]
device_id = personal_config["my_device"]
pin_map = {}


def main():
    from gpiozero import DigitalInputDevice, DigitalOutputDevice
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
        if not payload.keys() >= {"pin", "state"}:
            print("Error, invalid message")
            return
        pin, state = payload["pin"], payload["state"]
        if pin_map[pin]:
            pin_map[pin].value = state
            print("Change state of pin {} to {}".format(pin, state))

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

    def on_action(pin, state):
        json_var = json.dumps({"pin": pin, "state": state})
        mqttc.publish(f'{topic}/{device_id}/input', json_var, 0, False)

    mqttc = mqtt.Client(personal_config["my_client"])
    mqttc.on_connect = on_connect
    mqttc.connect("test.mosquitto.org", 1883, 60)
    mqttc.loop_forever()
    
    
thread = Thread(target=main)
thread.start()
