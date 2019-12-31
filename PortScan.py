#! python3

import socket #scan module : node to node connection
import sys  #system module
from datetime import datetime as dt #import with alias 

def nl(): #function to create new lines
    print('\n')

#Ask for input
RServer = input("Enter a remote host to scan: ")
RServerIP = socket.gethostbyname(RServer) #translate hostname to IPv4

#Print a banner with information
print ("-" * 60)
nl()
print ("Please wait, scanning remote host", RServerIP)
nl()

#Check what time the scan started
t1 = dt.now()
print ("Time started: " + str(t1))
print ("-" * 60)
nl()

#Using the range function to speicify ports

#Error handling for catching errors:

try:
    for port in range (1,2): # pick the range (1,65535) 1 port at a time (will take forever v_v)
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPv4  SOCK_STREAM = port
     socket.setdefaulttimeout(1) # 1 sec to try to connect to a port, if not responding, go to the next one
     result = s.connect_ex((RServerIP, port)) # returns an error indicaton
     print("Checking port {}".format(port)) # display what port the script is scanning
    if result == 0:
        nl()
        print ("[+]Port{}:      Open".format(port)) # the port is open
        nl()
    else:
        print("-" * 60)
        nl()
        print("[-]No ports are opened on this address...")
        nl()
        print("-" * 60)
    s.close() # close the connection
    
#Some exceptions:
    
except KeyboardInterrupt:
    print ("You pressed Ctrl + C. Exiting program")
    sys.exit()
    
except socket.gaierror:
    print ("Hostname could not be resolved. Exiting program")
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

