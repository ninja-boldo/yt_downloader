from typing import List
from enum import Enum
from pywhispercpp.model import Model
import models_whisper

class whisper_models(Enum):
    large_turbo = ""
    SUMMER = ""
    AUTUMN = ""
    WINTER = ""


class transcriber:
    def __init__(self, file_paths: List[str] = [], model: str = "large-v3-turbo-q5_0") -> None:
        self.whisper_models = models_whisper.get_supported_models()
        self.file_paths = file_paths
        if model in self.whisper_models:
            self.model_name = model
            self.model_whisper = Model(model=model)
        else:
            raise Exception(f"""the supplied model: {model} wasnt one of the supported ones,
                            with this being the accepted ones: {self.whisper_models}""")
    
    def is_valid_list(self, list_):
        # also implement checking if it contains only strings
        return (isinstance(list_, list) and len(list_) > 0)
    
    
    def transcribe(self, file_paths: str | List[str], language='en') -> List[str]:
        """Transcribe audio file using Whisper model"""
        print(f"Transcribing: {file_paths} (language: {language})")
        try:
            results = []
            if self.is_valid_list(list_=file_paths):
                for path in file_paths:
                    segments = self.model_whisper.transcribe(path, language=language)
                    result = "".join(segment.text for segment in segments)
                    results.append(result)
                    #print(f"Transcription complete: {result[:100]}...")
                    
            elif isinstance(file_paths, str):
                segments = self.model_whisper.transcribe(file_paths, language=language)
                result = "".join(segment.text for segment in segments)
                results.append(result)
                #print(f"Transcription complete: {result[:100]}...")
                
            return results
        
        except Exception as e:
            print(f"Transcription error: {e}")
            return [f"Error: Failed to transcribe audio - {str(e)}"]