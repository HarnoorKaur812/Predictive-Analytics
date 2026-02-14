import sys
import os
import shutil
import re
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def create_mashup(singer, n, duration, output_file):
    download_dir = 'downloads'
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
    os.makedirs(download_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'referer': 'https://www.google.com/',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
    }

    print(f"Searching and downloading {n} videos for {singer}...")
    with YoutubeDL(ydl_opts) as ydl:
        try:
            search_query = f"ytsearch{n}:{singer} official audio"
            ydl.download([search_query])
        except Exception:
            pass 

    combined = AudioSegment.empty()
    files = [f for f in os.listdir(download_dir) if f.endswith('.mp3')]
    
    if not files:
        raise Exception("YouTube is currently blocking cloud requests (403). Try again or test locally.")

    print(f"Trimming {n} files to {duration} seconds each...")
    for file in files[:n]:
        path = os.path.join(download_dir, file)
        try:
            audio = AudioSegment.from_file(path)
            cut_audio = audio[:duration * 1000] 
            combined += cut_audio
        except Exception:
            continue
    
    combined.export(output_file, format="mp3")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 102303993.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    try:
        singer_name = sys.argv[1]
        num_videos = int(sys.argv[2])
        audio_dur = int(sys.argv[3])
        out_name = sys.argv[4]

        if num_videos <= 10 or audio_dur <= 20:
            print("Error: N must be > 10 and Y must be > 20.")
            sys.exit(1)

        create_mashup(singer_name, num_videos, audio_dur, out_name)
        print("SUCCESS: Mashup Complete.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)