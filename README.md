# M2M SIM Workflow Demo

A Python-based demonstration of Machine-to-Machine (M2M) SIM card communication using AT commands.

This project demonstrates the complete workflow of an M2M SIM card, including:

- Network registration
- Signal strength monitoring
- SMS sending and receiving
- SIM information retrieval
- Packet network attachment
- Internet connectivity verification
- HTTP communication
- MQTT communication

---

# Project Objective

The purpose of this project is to understand how an M2M SIM communicates with the cellular network and how IoT devices use cellular connectivity for messaging and internet-based communication.

---

# Workflow

```
                   +----------------------+
                   |   Python Application |
                   +----------+-----------+
                              |
                         pySerial Library
                              |
                              |
                    USB / UART Communication
                              |
                              |
                   +----------v-----------+
                   | Cellular Modem       |
                   | (SIM7600 / EC25 etc.)|
                   +----------+-----------+
                              |
                         AT Commands
                              |
                   +----------v-----------+
                   |     M2M SIM Card     |
                   +----------+-----------+
                              |
                       Cellular Network
                    (2G / 3G / LTE / NB-IoT)
                              |
               +--------------+--------------+
               |                             |
             SMS                        Mobile Data
               |                             |
        SMS Gateway                   Internet
                                             |
                                     Cloud Server
                                             |
                                  HTTP / MQTT Communication
```

---

# Repository Structure

```
m2m-sim-workflow-demo/
│
├── README.md
├── requirements.txt
├── send_sms.py
├── receive_sms.py
├── check_network.py
├── signal_strength.py
├── sim_information.py
├── packet_network.py
├── internet_test.py
├── send_http_data.py
├── mqtt_publish.py
└── docs/
      workflow.png
```

---

# Requirements

- Python 3.x
- pySerial
- requests
- paho-mqtt

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Hardware Requirements

- Linux PC
- USB LTE/GSM Modem
- Active M2M SIM Card
- USB Cable

---

# Features

## 1. Network Registration

Checks whether the SIM is registered with the mobile operator.

AT Command

```
AT+CREG?
```

Expected Output

```
+CREG: 0,1
```

---

## 2. Signal Strength

Measures cellular signal quality.

AT Command

```
AT+CSQ
```

Example

```
+CSQ: 22,99
```

---

## 3. Send SMS

Uses AT commands to send an SMS.

AT Commands

```
AT+CMGF=1
AT+CMGS="+911234567890"
```

---

## 4. Read SMS

Lists SMS messages stored on the SIM.

AT Command

```
AT+CMGL="ALL"
```

---

## 5. SIM Information

Retrieves SIM and modem details.

Commands

```
AT+CCID
AT+CIMI
AT+CGSN
AT+CNUM
```

Returns

- ICCID
- IMSI
- IMEI
- Phone Number (if available)

---

## 6. Packet Network Attachment

Checks if the SIM is attached to the data network.

AT Command

```
AT+CGATT?
```

Expected Output

```
+CGATT: 1
```

---

## 7. Internet Connectivity

Verifies that the modem has internet access by sending an HTTP request.

Example

```python
requests.get("https://httpbin.org/ip")
```

---

## 8. HTTP Communication

Uploads JSON data to a cloud endpoint.

Example Payload

```json
{
  "device": "SIM7600",
  "temperature": 27,
  "humidity": 64
}
```

---

## 9. MQTT Communication

Publishes data to an MQTT broker.

Example Topic

```
m2m/demo
```

Example Message

```
Temperature=27
```

---

# M2M Communication Flow

```
Device
   │
   ▼
Python Application
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
LTE / GSM Network
   │
   ├────────────► SMS Gateway
   │
   └────────────► Internet
                      │
                      ▼
              Cloud Server
                HTTP / MQTT
```

---

# Skills Demonstrated

- Python Programming
- AT Command Communication
- pySerial
- Cellular Network Registration
- GSM/LTE Communication
- SMS Messaging
- M2M SIM Management
- HTTP APIs
- MQTT Protocol
- IoT Communication
- Cellular Internet Connectivity

---

# Future Enhancements

- GPS Data Retrieval
- HTTPS Communication
- SSL-enabled MQTT
- Remote Device Monitoring
- Automatic Reconnection
- SIM Status Dashboard

---

# References

- 3GPP AT Command Specifications
- pySerial Documentation
- Requests Library
- Eclipse Paho MQTT

---

# Author

**Your Name**

M2M SIM Workflow Demonstration using Python.
