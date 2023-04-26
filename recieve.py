import paho.mqtt.client as mqtt

# Define callback functions
def on_connect(client, userdata, flags, rc):
    client.subscribe("data")

# Create MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect

# Connect to broker
client.connect("localhost", 1883)

# Start the loop to process incoming messages
client.loop()