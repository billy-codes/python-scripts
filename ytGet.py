#!/usr/bin/env python3

# First Intall pytube:
#   python3 -m pip install pytube
from pytube import YouTube

url = "https://www.youtube.com/watch?v=hGIW2fDb0jg&t=1837s"

yt_obj = YouTube(url)
for stream in yt_obj.streams:
    print(stream)