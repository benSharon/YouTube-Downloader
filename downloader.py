import time
import os

from pytubefix import YouTube, Channel
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable

USER = os.getlogin()  # PC user


def download_single_video(video_url):
    try:
        youtube_video = YouTube(video_url, on_progress_callback=on_progress)
        path = f"C:\\Users\\{USER}\\Downloads\\{youtube_video.author}"
        print("Downloading...")
        # video_stream = youtube_video.streams.get_by_resolution(resolution="480")
        # for some reason, resolution="480" is giving 'NoneType' object has no attribute 'download'.
        video_stream = youtube_video.streams.get_highest_resolution()
        video_stream.download(path)
    except VideoUnavailable as e:
        print(f"VideoUnavailable Error: {e}. The video may be restricted or unavailable.\n")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_channel_urls(channel):
    try:
        channel_url = Channel(channel)
        url_list = [channel_video.watch_url for channel_video in channel_url.videos]
        print(url_list)
    except Exception as e:
        print(f"An error occurred: {e}\n")


def download_all_channel_videos(channel):
    try:
        channel_url = Channel(channel)
        print(f"{channel_url.channel_name} has {len(channel_url.videos)} videos.")
        print("Commencing download...\n")
        for channel_video in channel_url.videos:
            download_single_video(channel_video.watch_url)
            time.sleep(3.0)
    except Exception as e:
        print(f"An error occurred: {e}\n")
