#Importing libraries
import ipaddress
import os
from datetime import datetime
import platform
import re
import socket
import time
import threading
from queue import Queue

#initializing variables
ports = 0
times = datetime.now()
hope = threading.Lock() # Create a lock object to ensure thread safety
socket.setdefaulttimeout(0.25)# Set the default timeout for socket operations to 0.25 seconds
ipsactivess = 0

listipvalide = []
list2ping = []

#Function definition:IP Address Availability Check
def ping(ipvalid):
    global ipsactivess
    if platform.system().lower() == 'windows':
        answer = os.system('ping -n 1 -w 500 ' + ipvalid + ' > nul')
        if answer == 0:
            list2ping.append(ipvalid)
            ipsactivess += 1
    if platform.system().lower() == 'linux':
        answer = os.system('ping -c 1 -W 1 ' + ipvalid + '> /dev/null')
        if answer == 0:
            list2ping.append(ipvalid)
            ipsactivess += 1


###############################################################################
#Function definition: Input Validation

def validate_ipaddress(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as errorCode:

        pass
        return False


def main():
    global ipno
    global ipaddr
    ipno = False
    ipaddr = input(" ip: \n")
    while ipno != True:
        if (validate_ipaddress(ipaddr) == False):
            print(" IP is not valide  ")
            ipno = False
            ipaddr = input(" ip:\n")
        else:
            print("IP {} valid".format(ipaddr))
            ipno = True


if __name__ == "__main__":
    main()
##################################################################################
while True:
    print("################################################")
    numberips = input("number of IPs: ")
    print('################################################')
    if numberips.isdecimal() == False:
        print("invalide number. ")
        continue
    break
#################################################################################
#IP adress generation
if numberips.isdecimal() == True:
    numberips = int(numberips)
count = 0
while count < numberips:
    listipvalide.append(ipaddr)
    sum = int(ipaddress.IPv4Address(ipaddr))
    sum = sum + 1
    ipaddr = str(ipaddress.IPv4Address(sum))
    count = count + 1
lengthlist = len(listipvalide)
###################################################################################
#IPs availibility check
counting = 0
while counting < lengthlist:
    dos = listipvalide[counting]
    ping(dos)
    counting += 1
ipspinglistt = len(list2ping)
pinglst = 0
if pinglst < ipspinglistt:
    print('IPs Actives: ')
    while pinglst < ipspinglistt:
        print(list2ping[pinglst])
        pinglst += 1
    print('################################################')
    print('')


#####################################################################################
#Port Scanner
def scanner(port, ipss):
    global ports
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connecting = s.connect((ipss, port))
        with hope:
            print(ipss, port, ' port is up ')
            ports += 1
        connecting.close()
    except:
        pass


def threader():
    while True:
        slave = queu1.get()
        scanner(slave, ipss)
        queu1.task_done()


queu1 = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

ipports = 0

while True:
    try:
        nprt = int(input("number of ports to scan :"))
        break
    except ValueError:
        continue

while ipports < ipspinglistt:
    ipss = list2ping[ipports]
    for slave in range(1, nprt):
        queu1.put(slave, ipss)
    ipports += 1
    queu1.join()

#################################################################################

print('')
print('active IPs : ', ipsactivess)
print('Ports:', ports)
timett = datetime.now() - times
print('execution complete in {}'.format(timett))