# Physical Device

## Script

Create *personal_config.py* in the **same directory** as *copernicus.py*. Dictionary in the file should look like this:
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

## System daemon setup (Raspberry Pi OS)

In order to run *copernicus.py* at the system boot You have to create corresponding system service. <br/><br/>
***NOTE*** <br/>
***It is neccessary to install dependecies form *requirements.txt* globally, using pip3.*** 

### Steps

1.  Create file (using **sudo**) *copernicus.service* in */etc/systemd/system*. The file should contain following entries:
```
[Unit]
Description=Copernicus Node-RED plugin
After=multi-user.target

[Service]
WorkingDirectory=<absolute path to directory containing both copernicus.py and personal_config.py>
User=pi
Type=simple
ExecStart=/usr/bin/python3 <absolute path to copernicus.py>
Restart=on-failure
StartLimitBurst=0

[Install]
WantedBy=multi-user.target

```

2.  Enable automatic service run at next boot: ```sudo systemctl enable copernicus.service```<br/> 
If you want to execute it immediately use also ```sudo systemctl start coperncius.service```

To check service status use ```systemctl status copernicus.service```<br/>
To get more information use ```journalctl -u copernicus.service```
<br/>
It is highly advised to get familiar with mauals for both commands.
