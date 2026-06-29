import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("test.mosquitto.org",1883,60)

client.publish(
    "m2m/demo",
    "Temperature=26"
)

client.disconnect()