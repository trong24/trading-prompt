from yt_dlp import YoutubeDL

def download_youtube_audio_as_m4a(url):
    """
    Downloads the audio from a YouTube video as an M4A file.

    Args:
        url (str): The URL of the YouTube video.
    """
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',  # Prioritize M4A audio, fallback to best available
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',  # Optional: specify preferred quality (e.g., '192' for 192kbps)
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template (e.g., Video Title.m4a)
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_audio_as_m4a(video_url)