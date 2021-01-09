# A simple port scanner using socket module 
from socket import *
import time

target = input("Enter IP Address: ")
T_IP = gethostbyname(target)
# Port Range format is START_PORT:END_PORT
portRange = input("Enter Port Range (0:65535): ")
print("IP Address: ", T_IP)
portRanges = portRange.split(':')
startTime = time.time()
for i in range(int(portRanges[0]), int(portRanges[1])):
	s = socket(AF_INET, SOCK_STREAM)

	conn = s.connect_ex((T_IP,i))
	if(conn == 0):
		print('Port %d: OPEN' % (i,))
	s.close()
print('Total Time: ', time.time() - startTime)