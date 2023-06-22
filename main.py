import socket
import os

def scan_ports(ip_address):
    # Scan ports from 1 to 65535
    for port in range(1, 65536):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set a timeout for the connection
            sock.settimeout(1)
            
            # Attempt to connect to the IP address and port
            result = sock.connect_ex((ip_address, port))
            
            if result == 0:
                print(f"Port {port} is open")
                
            # Close the socket
            sock.close()
            
        except socket.error:
            print("Could not connect to the server")
            sys.exit()

ip_address=input("Enter IP: ")

scan_ports(ip_address)
