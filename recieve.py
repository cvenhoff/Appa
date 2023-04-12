import paho.mqtt.client as mqtt

# Define callback functions
def on_connect(client, userdata, flags, rc):
    client.subscribe("data")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Create MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect("localhost", 1883)

# Start the loop to process incoming messages
client.loop_forever()