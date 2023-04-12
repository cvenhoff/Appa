import can
import mqtt_utils
import csv
import queue
import cantools
import datetime
import csv_utils

######
bustype = 'socketcan_ctypes' 
dbc_param = 'FromEmergencySystemGyroRot'
######

#prepare csv
filename = 'dump.csv'
csv_utils.init_csv(filename)

# initialize the bus using the default interface
#print(can.interface.detect_available_configs())
bus =  can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')

# specify the dbc file that will be used to decode the messages
dbc_file = 'CarCan.dbc'
dbc = cantools.database.load_file(dbc_file)

# initialize a queue to store incoming CAN messages
message_queue = queue.Queue()

def process_messages():
    while True: 

        # retrieve the next message from the queue  
      
        msg = message_queue.get()

        # decode the message using the dbc file
        decoded_message = dbc.decode_message(dbc_param, msg.data)

        for name in decoded_message:
            # send the decoded message as a MQTT message
            mqtt_utils.publish(name,decoded_message[name])
            # write in csv
            with open(filename, 'a', newline='') as csvfile:
                t = datetime.datetime.now()
                t = t.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
                writer = csv.writer(csvfile)
                writer.writerow(["","",0,t,t,t,decoded_message[name],name,"mqqt_consumer","local","data"])

            
def receive_messages():
    while True:
        # receive a message from the CAN bus
        try:
            msg = bus.recv()
            print(msg)
        except:
            continue
        
        # put the message in the queue for processing
        message_queue.put(msg)

