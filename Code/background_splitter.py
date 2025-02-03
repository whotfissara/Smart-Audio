from pydub import AudioSegment
import random
import os

for i in range(13):
    sound2 = AudioSegment.from_file(f"Background Noise/background{i + 1}.mp3")
    #print(f"noise: {sound2.dBFS}")
    for j in range(5):
        sound = 0
        rand_time = random.randint(0, len(sound2) - 4000)
        sound = sound2[rand_time:rand_time + 4000] 
        #print(f"voice: {sound.dBFS} sound: {sound}")
        sound.export(f"new_back/background{i + 1}_{j+1}.mp3", format='mp3')



