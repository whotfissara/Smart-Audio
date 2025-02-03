from pydub import AudioSegment
import random
import os

class AudioAugmenter:
    def __init__(self, input_folder="orig_name", output_folder="final_name", background_folder="new_back"):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.background_folder = background_folder
        self.target_gain = -22
        os.makedirs(self.output_folder, exist_ok=True)


    def augment_audio(self, filenames, num_variations=5):
        augmented_files = []
        for filename in filenames:
            input_path = os.path.join(self.input_folder, filename)  # Correct input path

            for j in range(num_variations):
                audio = AudioSegment.from_file(input_path)

                audio = audio + (self.target_gain - audio.dBFS)
                silence = AudioSegment.silent(duration=1000)
                audio = silence + audio + silence

                # Overlay with random background
                rand1 = random.randint(1, 10)
                rand2 = random.randint(1, 5)
                background_filename = f"background{rand1}_{rand2}.mp3"
                background_path = os.path.join(self.background_folder, background_filename)

                if os.path.exists(background_path):  # Ensure background file exists
                    background = AudioSegment.from_file(background_path)
                    background = background + (self.target_gain - background.dBFS)
                    audio = background.overlay(audio)

                # Export
                output_filename = f"{filename[:-4]}_{j + 1}.mp3"  # Avoid double .mp3
                output_path = os.path.join(self.output_folder, output_filename)
                audio.export(output_path, format='mp3')
                augmented_files.append(output_filename)  # Store filename only

        return augmented_files
