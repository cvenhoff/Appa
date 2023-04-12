import json
import paho.mqtt.client as mqtt

# initialize the MQTT client

client = mqtt.Client(client_id="Ecogenium")

def connect():
    client.connect("10.8.0.1", 1883)
    client.loop_start()

def publish(sensor_name, sensor_value):
        payload = json.dumps({
            sensor_name:sensor_value
        })
        client.publish(topic="data", payload=payload)
    

   
