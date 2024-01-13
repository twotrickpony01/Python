import socket

def socket_check(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)):
        return "Port " + str(port) + " is open."
    else:
        return "Port " + str(port) + " is closed."