import write
import mqtt_utils
import threading
import os

# start hat
os.system('sudo /sbin/ip link set can0 down')
os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')

# start the process_messages and receive_messages functions as separate threads
mqtt_utils.connect()
write.get_messages()