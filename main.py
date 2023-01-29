from pytube import YouTube

# Get the link of the video you want to download
link = "https://www.youtube.com/watch?v=6HRON_6yPII&ab_channel=NationalGeographicIndia"

# Create a YouTube object
yt = YouTube(link)

# Get the video with the highest resolution
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Download the video
video.download()