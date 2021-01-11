# A simple ping sweeping script to scan live hosts over a network
# Uses ICMP to send ECHO requests to hosts
# Future Features: Multithreading
import os, platform
from datetime import datetime


network = input("Enter IP Address: ")
ip_address = network.split(".")
p = "."

startRange = int(input("Starting Range (min = 1): "))
endRange = int(input("Ending Range (max = 254): "))
if(int(startRange) > 0 & int(endRange) < 254):
	endRange = int(endRange) + 1
else:
	print("Invalid Range")

# Simulates ping command using cmd or terminal
def ping_Command(os):
	if os == "Windows":
		return "ping -n 1 "
	else:
		return "ping -c 1 "

startTime = datetime.now()
print("Scanning Live Hosts")

for ip in range(startRange, endRange):
	address = ip_address[0] + p + ip_address[1] + p + ip_address[2] + p + str(ip)
	command = ping_Command(platform.system()) + address
	response = os.popen(command)

	for line in response.readlines():
		if(line.count("TTL")):
			print(address, " --> Live")


endTime = datetime.now()
duration = endTime - startTime
print("Scan Complete: ",duration)
