# A simple bandwidth monitoring tool
# that displays amount of received 
# and sent data since the computer
# was switched on

# Requirements: pip3 install psutil
# rx -> Received
# tx -> Sent

import time
import psutil

def conversion(value): # to megabytes
    return value/1024/1024.
        
def displayUnit(rx, tx):
    print("Total Received: ","%0.3f" % conversion(rx), "MB")
    print("Total Sent: ","%0.3f" % conversion(tx), "MB")

timeInterval = 3 # run every 3 seconds

while True:
    # get new rx and tx values
    new_rx = psutil.net_io_counters().bytes_recv
    new_tx = psutil.net_io_counters().bytes_sent
    displayUnit(new_rx, new_tx)
    time.sleep(timeInterval)
    

