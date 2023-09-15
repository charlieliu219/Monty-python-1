import youtube_dl

def extract_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extract_flat': 'in_playlist',
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'quiet': False,
        'verbose': True

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

video_url = 'https://www.youtube.com/watch?v=cIYfiRyPi3o&ab_channel=rubatirabbit'
extract_audio(video_url)
