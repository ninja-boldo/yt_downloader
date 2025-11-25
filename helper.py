import os
from pathlib import Path
import uuid
from typing import List
import subprocess

class helper:
    def __init__(self) -> None:
        pass
    
    def get_file_path(self) -> str:
        return str(os.path.abspath(__file__))
    
    def get_folder_files(self, path=".") -> List[str]:
        if path == ".":
            path = self.get_file_path()
        return os.listdir(path)
    
    def write_txt(self, text: str = "", filename: str | None = None):
        if filename is None:
            filename = str(uuid.uuid4())
        with open(f"{filename}.txt", "a") as f:
            f.write(text)
    
    def mergeVideos(self, video: str, output: str = "output.mp4"):
        """Merge video with existing output.mp4 (or create new if doesn't exist)"""
        try:
            # Ensure video path has .mp4 extension
            video_path = Path(video)
            if video_path.suffix != '.mp4':
                video_path = video_path.with_suffix('.mp4')
            
            if not video_path.exists():
                print(f"Error: Video file not found: {video_path}")
                return False
            
            video_dir = video_path.parent
            output_path = video_dir / output
            
            # If output doesn't exist, just copy the video as output
            if not output_path.exists():
                print(f"Creating new {output} with {video_path.name}")
                result = subprocess.run([
                    'ffmpeg', '-i', str(video_path), '-c', 'copy', str(output_path)
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    print(f"FFmpeg error: {result.stderr}")
                    return False
                    
                print(f"✓ Created {output}")
                return True
            
            # Output exists, merge with it using filter_complex for proper concatenation
            print(f"Merging {video_path.name} with {output}...")
            temp_out = video_dir / f"temp_{output}"
            
            result = subprocess.run([
                'ffmpeg', '-y',
                '-i', str(output_path),
                '-i', str(video_path),
                '-filter_complex', '[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[outv][outa]',
                '-map', '[outv]',
                '-map', '[outa]',
                '-c:v', 'libx264',
                '-preset', 'medium',
                '-crf', '23',
                '-c:a', 'aac',
                str(temp_out)
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"FFmpeg error: {result.stderr}")
                return False
            
            # Replace output
            output_path.unlink()
            temp_out.rename(output_path)
            
            print(f"✓ Merged {video_path.name} → {output}")
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            return False