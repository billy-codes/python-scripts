#!/usr/bin/env python3

# First Intall pytube:
#   python3 -m pip install pytube
from pytube import YouTube

url = "https://www.youtube.com/watch?v=fLz5OUYxR6Q"

yt_obj = YouTube(url)

yt_Title = yt_obj.title
yt_Duration = yt_obj.length / 60 # in minutes
yt_Views = yt_obj.views

# progressive means both audio and video
yt_Filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
print("Available Quality:")
def get_Resolution(yt_Filters):
    i = 0
    for yt_mp4 in yt_Filters:
        #print(yt_mp4.__dict__.keys()) # use __dict__.keys() to find all object attributes
        print(f"[{i}]", yt_mp4.resolution)
        i+=1
def download_Video(yt_Filters, index):
    i = 0
    for yt_mp4 in yt_Filters:
        if i == index:
            try:
                yt_obj.streams.get_by_itag(yt_mp4.itag).download()
                print("Download Successful")
            except Exception as e:
                print(e)
        else:
            continue
        i+=1

get_Resolution(yt_Filters)
resolution = input("Enter Option: ")
download_Video(yt_Filters, int(resolution))


# for stream in yt_obj.streams:
#     print(stream.itag)
