from pyt2s.services import stream_elements
import os

class StreamElementsGenerator:
    def __init__(self, name, output_folder="orig_name"):
        self.name = name
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_tts(self):
        filenames = []
        for voice in stream_elements.Voice:
            if voice == stream_elements.Voice.cmn_CN_Wavenet_D:  # Example stopping condition
                break
            filename = f"{voice}.mp3"
            filepath = os.path.join(self.output_folder, filename)
            data = stream_elements.requestTTS(self.name, voice.value)
            with open(filepath, 'wb') as file:
                file.write(data)
            filenames.append(filename)  # Store only the filename, not full path
        return filenames
