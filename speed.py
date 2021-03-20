# A simple Speedtest script to test
# you internet download and upload
# speed

# Requirements:
# pip3 install speedtest-cli

import speedtest

# create instance of Speedtest
s = speedtest.Speedtest()


print("Download Speed: ", s.download())