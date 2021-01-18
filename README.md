# Node Red RPI Copernicus NG
A project for IoT classes at AGH UST, Poland

Developed by:
- Krzysztof Nalepa, [@kraleppa](https://github.com/kraleppa)
- Jakub Solecki, [@jakubsolecki](https://github.com/jakubsolecki)
- Mateusz Obrzut, [@matt628](https://github.com/matt628)
- Krzysztof Widenka, [@krzwid](https://github.com/krzwid)

The aim of the project was to develop a software agent implementation for the device
VirtualCopernicusNG enabling its management and control using the Node Red tool.
The project developed sample programs. 

## Node-RED

Dowload local Node-RED from website: https://nodered.org/docs/getting-started/local

Run it by typing in terminal `node-red`.

Node-RED is hosted now locally. 
Default server is `http://127.0.0.1:1880/`

Import `flows.json` from `Flows` directory, deploy the flows on Node-RED. 

### Building custom flows

It's possible to build custom flows.
1. Choose button 
2. Assign actions to button
3. Click deploy
4. Initialize  device again

![](docs/create_flows.gif)

## Devices

Both of the devices use flows described in the corresponding [README](./Flows/README.md)

### Physical device
Usage of physical device is described in the corresponding [README](./physical_device/README.md) 

### Virtual device
Usage of virtual device is described in the corresponding [README](./virtual_device/README.md) 
