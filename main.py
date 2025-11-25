from fetch import downloader
from helper import helper

downloader_instance = downloader()
#transcriber_instance = transcriber()
helper_instance = helper()

urls = ["https://www.youtube.com/watch?v=cSOQPJl53Ng", "https://www.youtube.com/watch?v=34mk2F4iff4"]

file_paths = downloader_instance.download(urls=urls, only_audio=False)


for idx, path in enumerate(file_paths):
    print(f"path: {path}")
    helper_instance.mergeVideos(video=path)
