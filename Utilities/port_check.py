import socket

def socket_check():
    ip = raw_input("Please give an IP address to search: ")
    port = int(raw_input("Please give a socket to check: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)):
        return "Port " + str(port) + " is open."
    else:
        return "Port " + str(port) + " is closed."

print socket_check()
