import socket

def get_current_ip(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

# Replace 'yourhostname.ddns.net' with your actual hostname
hostname = 'loggingpi.hopto.org'

current_ip = get_current_ip(hostname)
