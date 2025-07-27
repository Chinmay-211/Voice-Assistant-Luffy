from pytube import YouTube

def download_youtube_video(url, save_path='.'):
    try:
        yt = YouTube(url)
        
        # Filter for progressive streams (video + audio) with highest resolution
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        if video_stream:
            video_stream.download(output_path=save_path)
            print(f"Video downloaded successfully from YouTube: {save_path}/{video_stream.default_filename}")
        else:
            print("No suitable video stream found.")
    
    except Exception as e:
        print(f"Failed to download the YouTube video: {e}")

# Example usage
url = 'https://www.youtube.com/shorts/PbSy3PpC0qc'  # Replace with your YouTube URL
download_youtube_video(url)
