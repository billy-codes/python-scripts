#!/usr/bin/env python3

# First Intall pytube:
#   python3 -m pip install pytube
from pytube import YouTube

url = "https://www.youtube.com/watch?v=hGIW2fDb0jg&t=1837s"

yt_obj = YouTube(url)

yt_Title = yt_obj.title
yt_Duration = yt_obj.length / 60 # in minutes
yt_Views = yt_obj.views
for stream in yt_obj.streams:
    print(stream.itag)