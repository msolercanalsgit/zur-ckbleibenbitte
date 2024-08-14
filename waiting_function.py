import socket
import time

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False

while not check_internet():
    print("No internet connection. Retrying in 5 seconds...")
    time.sleep(5)

print("Internet connection established! Continuing execution...")
# Your code continues here...