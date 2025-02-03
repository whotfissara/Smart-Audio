from gtts import gTTS
import os

class TTSGenerator:
    def __init__(self, name, output_folder="orig_name"):
        self.name = name
        self.output_folder = output_folder
        self.lang_variants = [
            ['en', 'com.au'], ['en', 'co.uk'], ['en', 'us'], ['en', 'ca'], ['en', 'co.in'],
            ['en', 'ie'], ['en', 'co.za'], ['en', 'com.ng'], ['fr', 'ca'], ['fr', 'fr'],
            ['pt', 'com.br'], ['pt', 'pt'], ['es', 'com.mx'], ['es', 'es'], ['es', 'us'], ['zh-CN', 'ca']
        ]
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_tts(self):
        filenames = []
        for lang in self.lang_variants:
            filename = f"{self.name}_{lang[0]}_{lang[1]}.mp3"
            filepath = os.path.join(self.output_folder, filename)
            tts = gTTS(text=self.name, tld=lang[1], lang=lang[0], slow=False)
            tts.save(filepath)
            filenames.append(filename) 
        return filenames
