# A simple Speedtest script to test
# you internet download and upload
# speed

# Requirements:
# pip3 install speedtest-cli

import speedtest
import time

# initialization
s = speedtest.Speedtest()
timeStart = time.time()

print("Testing Speed...")

print("Download Speed: ", s.download())
print("Upload Speed: ", s.upload())

print("Total Time: ", round(time.time() - timeStart,2),"(s)")