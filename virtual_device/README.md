# Virtual Device

## Usage

Create personal_config.py file within personal_config dictionary.
This dictionary should contain three entries.
```
personal_config = {
    "my_device": "1", # unique for each deivice
    "my_client":"your_unique_client_id",
    "my_topic":"rpi/gpio",
}
```

-`my_device`
-`my_client`
-`my_topic`

### Node-RED
Dowload local Node-RED from website: https://nodered.org/docs/getting-started/local

Run it by typing in terminal `node-red`.

Node-RED is hosted now locally. 
Default server is `http://127.0.0.1:1880/`

Import `flows.json`, deploy the flows. 

### Virtual Device
In `virtual_device` folder run `python copernicus.py`
On Node-RED initialize virtual device by `init` button.
After initialization success message in console:
```
Initialized pin 11 as DigitalInput
Initialized pin 12 as DigitalInput
Initialized pin 16 as DigitalOutput
Initialized pin 21 as DigitalOutput
Initialized pin 22 as DigitalOutput
```


VirtualDevice can contain DigitalInput and DigitalOutput devices.
<ul>
    <li>DigitalOutput - f.e. LED, Buzzer</li>
    <li>DigitalInput - f.e Button</li>
</ul>

VirtualCopernicusDevice is equipped in:
<ul>
    <li>two LEDs onpins 21, 22 </li>
    <li> one buzzer on pin 16</li>
    <li> two buttons on pins 11, 12</li>
</ul>


## Building own flows

It's possible to build own flows.

![](docs/moj.gif)


