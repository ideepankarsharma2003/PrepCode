from pytube import Playlist , YouTube
import time
from sys import argv

# playlist_link = argv[1]
# folder = argv[2]

playlist_link = "https://youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH"
folder = "C:\Deepankar\CampusXDS"

# print(f'playlist link: {playlist_link}')
# print(f'download folder: {folder}')

videos=list(Playlist(playlist_link))

for i in range(len(videos)):
    for _ in range(5):
        try:
            yt   = YouTube(videos[i], use_oauth=True, allow_oauth_cache=True)
            yd = yt.streams.get_highest_resolution()
            video_title = yt.title   # title of video
            video_views = yt.views   # views in video
            video_length = yt.length # length of video in seconds
            video_size = yd.filesize # size of video in bytes

            print("\nTitle: ", video_title)
            print("Views: ", video_views)
            print("Length: ", video_length//60, "minutes", video_length%60, "seconds")
            print("Size: ", video_size/(2**20), "MB")

            time.sleep(1)
            print("Donwloading... ")

            # Add folder path here
            yd.download()

            print("Download complete!")
            print("\n------------------------------------")

        except Exception:
            print(f"\nAn error occurred")

print("\n ------------------Done------------------------\n")