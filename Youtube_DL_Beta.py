from __future__ import unicode_literals
import youtube_dl
import ffmpeg
import ffprobe3

def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "progress_hooks": [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/watch......"])
