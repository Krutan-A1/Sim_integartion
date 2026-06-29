# M2M SIM Workflow Demo

This project demonstrates the basic workflow of an M2M (Machine-to-Machine) SIM card using Python and AT commands.

## Features

- 📶 Check network registration
- 📡 Monitor signal strength
- 📩 Send SMS
- 📥 Read SMS
- 💳 Retrieve SIM information (ICCID, IMSI, IMEI)
- 🌐 Verify internet connectivity
- ☁️ Send HTTP requests
- 📡 Publish MQTT messages

## Workflow

```text
Python Script
      │
      ▼
  AT Commands
      │
      ▼
 Cellular Modem
      │
      ▼
    M2M SIM
      │
      ▼
 Cellular Network
      │
 ┌────┴────┐
 ▼         ▼
SMS     Internet
            │
            ▼
      HTTP / MQTT
      Cloud Server
```

## Requirements

- Python 3.x
- pySerial
- requests
- paho-mqtt

Install dependencies:

```bash
pip install -r requirements.txt
```

## Objective

Understand the workflow of M2M SIM cards, including message sending, network communication, and internet connectivity using Python and AT commands.
