import socket
import random
import time

target_ip = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = random._urandom(1024)
    sock.sendto(data, (target_ip, port))
    print("Packet sent")
    time.sleep(0.01)