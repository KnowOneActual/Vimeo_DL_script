import youtube_dl

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'extractor_args': {
            'vimeo': {
                'format': 'best',
            }
        },
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
video_url = 'https://vimeo.com/12345'  # Replace with your Vimeo video URL
output_folder = '/Users/'   # Replace with your desired output folder

download_video(video_url, output_folder)









