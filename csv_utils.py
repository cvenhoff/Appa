import csv
import datetime

def init_csv(filename):
    datatypes = ["#datatype","string","long","dateTime:RFC3339","dateTime:RFC3339","dateTime:RFC3339","double","string","string","string","string"]
    init = ["#default","mean","","","","","","","","",""]
    flags = ["#group","false","false","true","true","false","false","true","true","true","true"]
    header = ["",'result', 'table', '_start', '_stop', '_time', '_value', '_field', '_measurement', 'host', 'topic']

    with open(filename, 'a', newline='') as csvfile:
        t = datetime.datetime.now()
        t = t.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        writer = csv.writer(csvfile)
        writer.writerow(["","",0,t,t,t,"","","NEW RUN","",""])
    # Write header to file
    # with open(filename, 'r+', newline='') as f:
    #    f.seek(0)
    #    writer = csv.writer(f)
    #    writer.writerow(datatypes)
    #    writer.writerow(init)
    #    writer.writerow(flags)
    #    writer.writerow(header)
    #    f.seek(0, 2)
