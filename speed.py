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

# get the closes and best server available
s.get_best_server()

# results
print("Download Speed: ", s.download())
print("Upload Speed: ", s.upload())
print("Total Time: ", round(time.time() - timeStart,2),"(s)")

# store them in a dictionary 
# res = s.results.dict()
# print(res['download'], res['upload'], res['ping'])