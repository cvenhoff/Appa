import os
import write
import mqtt_utils
import threading

# start hat
os.system('sudo ifconfig can0 down')
os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

# start the process_messages and receive_messages functions as separate threads
mqtt_utils.connect()
t1 = threading.Thread(target=write.process_messages)
t2 = threading.Thread(target=write.receive_messages)
t1.start()
t2.start()