from tts_generator import TTSGenerator
from stream_elements_generator import StreamElementsGenerator
from audio_augmenter import AudioAugmenter

def main():
    name = "Elizabeth"
    
    tts_gen = TTSGenerator(name)
    google_tts_files = tts_gen.generate_tts()

    stream_gen = StreamElementsGenerator(name)
    stream_tts_files = stream_gen.generate_tts()

    all_tts_files = google_tts_files + stream_tts_files


    augmenter = AudioAugmenter()
    augmented_files = augmenter.augment_audio(all_tts_files, num_variations=1)

    print(f"Generated {len(augmented_files)} augmented audio files.")

if __name__ == "__main__":
    main()
