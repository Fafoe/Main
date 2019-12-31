#! python3

import socket
import sys
from datetime import datetime as dt #import with alias

def nl():
    print('\n')

#Ask for input
RServer = input("Enter a remote host to scan: ")
RServerIP = socket.gethostbyname(RServer)

#Print a banner with information
print ("-" * 60)
nl()
print ("Please wait, scanning remote host", RServerIP)
nl()
print ("-" * 60)

#Check what time the scan started
t1 = dt.now()
print ("The Scan started at " + str(t1))
nl()

#Using the range function to speicify ports

#Error handling for catching errors:

try:
    for port in range (1,2):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPv4  SOCK_STREAM = port
     result = s.connect_ex((RServerIP, port))
    if result == 0:
        nl()
        print ("[+]Port{}:      Open".format(port))
        nl()
    else:
        print("-" * 60)
        nl()
        print("[-]No ports are opened on this address...")
        nl()
        print("-" * 60)
    s.close()
    
    
except KeyboardInterrupt:
    print ("You pressed Ctrl + C")
    sys.exit()
    
except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()
    
except socket.error:
    print ("Could not connect to server")
    sys.exit()

#checking the time again
t2 = dt.now()

#How long did it take to scan
total = t2 - t1
print("-" * 60)
nl()
print ("Scanning completed in:", total)
print ("It is now " + str(t2))
nl()
print("-" * 60)

