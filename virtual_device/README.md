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

- `my_device` should be uniqe for each device 
- `my_client` should be unique for each device
- `my_topic` should be the same for for devices that need to communicate

### Virtual Device
In `virtual_device` directory run `python copernicus.py`
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
    <li>one buzzer on pin 16</li>
    <li>two buttons on pins 11, 12</li>
</ul>


