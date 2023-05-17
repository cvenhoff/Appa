import can
import mqtt_utils
import csv
import queue
import cantools
import datetime
import csv_utils
import os.path

######
bustype = 'socketcan_ctypes' 
######

#prepare csv
filename = 'dump.csv'
my_path = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(my_path, filename)
csv_utils.init_csv(csv_path)

# initialize the bus using the default interface
#print(can.interface.detect_available_configs())
bus =  can.interface.Bus(channel='can0', bustype=bustype)

# specify the dbc file that will be used to decode the messages
dbc_file = 'CarCan.dbc'
dbc_path = os.path.join(my_path, dbc_file)
dbc = cantools.database.load_file(dbc_path)

# initialize a queue to store incoming CAN messages
message_queue = queue.Queue()

def process_messages():
    while True: 
        try:
            # retrieve the next message from the queue  
            msg = message_queue.get()

            # decode the message using the dbc file
            print(msg.data)
            decoded_message = dbc.decode_message(msg.arbitration_id,msg.data)

            for name in decoded_message:
                # send the decoded message as a MQTT message
                mqtt_utils.publish(name,decoded_message[name])
                # write in csv
                with open(csv_path, 'a', newline='') as csvfile:
                    t = datetime.datetime.now()
                    t = t.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
                    writer = csv.writer(csvfile)
                    writer.writerow(["","",0,t,t,t,decoded_message[name],name,"mqqt_consumer","local","data"])
        except Exception as e:
            print("Error: " + repr(e))
            continue
            
def receive_messages():
    while True:
        # receive a message from the CAN bus
        try:
            msg = bus.recv(10.0)
            if(msg != None):
                # put the message in the queue for processing
                message_queue.put(msg)
        except Exception as e:
            print("Error: " + repr(e))
            continue

