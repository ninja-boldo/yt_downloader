import os
from typing import List
import uuid
from pytubefix import YouTube
from pytubefix.cli import on_progress

class downloader:
    def __init__(self, urls: List[str] | str = "", downloads_folder: str="downloaded_videos") -> None:
        if(isinstance(urls, str)):
            urls = [urls]
        self.urls = urls
        self.downloads_folder = downloads_folder
        self.full_download_path = f"{self.get_path()}/{self.downloads_folder}"
        self.filenames = []
        self.file_paths = []
        
        
    def get_file_path(self) -> str:
        return str(os.path.abspath(__file__))
    
    def get_path(self):
        full_path = self.get_file_path()
        parts = full_path.split("/")
        parts.pop(-1)
        folder_path = "/".join(parts)
        return folder_path
    
    def prettify_title(self, title: str):
        title = title.lower()
        title = title.replace(" ", "_")
        title = title.replace(".", "_")
        return title
    
    def download(self, urls: List[str] | str | None = None, only_audio: bool=True):
        if urls is None:
            urls = self.urls
        if isinstance(urls, str):
            urls = [urls]
            
        if only_audio:
            for url in urls:
                yt = YouTube(url, on_progress_callback=on_progress)

                ys = yt.streams.get_audio_only()
                if ys is not None:
                    filename = f"{self.prettify_title(yt.title)}.mp3"
                    ys.download(output_path=self.full_download_path, filename=str(uuid.uuid4()))
                    full_path = f"{self.full_download_path}/{self.prettify_title(yt.title)}.mp4"
                    self.filenames.append(filename)
                    self.file_paths.append(full_path)
                else:
                    print("No audio stream found for", url)
            
            return self.file_paths
        else:
            for url in urls:
                yt = YouTube(url, on_progress_callback=on_progress)
                

                ys = yt.streams.get_highest_resolution()
                if ys is not None:
                    filename = f"{self.prettify_title(yt.title)}.mp4"
                    ys.download(output_path=self.full_download_path, filename=filename)
                    full_path = f"{self.full_download_path}/{self.prettify_title(yt.title)}"
                    self.file_paths.append(full_path)
                    self.filenames.append(filename)
                else:
                    print("No audio stream found for", url)
            
            return self.file_paths
    