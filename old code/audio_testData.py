from gtts import gTTS
from pydub import AudioSegment
from pyt2s.services import stream_elements
import librosa
import random
import os

# https://www.mathworks.com/help/audio/ug/keyword-spotting-in-noise-using-mfcc-and-lstm-networks.html


'''if you want to run this you have to download ffmpeg and add it to your path, look up a youtube tutorial on 
how to do this or else AudioSegment will never find the correct path'''
arr = []

name = "stanley"

lang = [['en', 'com.au'], ['en', 'co.uk'], ['en', 'us'], ['en', 'ca'], ['en', 'co.in'] ,
        ['en', 'ie'], ['en', 'co.za'], ['en', 'com.ng'], ['fr', 'ca'], ['fr', 'fr'], 
        ['pt', 'com.br'], ['pt', 'pt'], ['es', 'com.mx'], ['es', 'es'], ['es', 'us'], ['zh-CN', 'ca']]

#google TTS
for i in range(len(lang)):
        tts = gTTS(text = name, tld = lang[i][1], lang = lang[i][0], slow = False)
        arr.append(f"{name}_{lang[i][0]}_{lang[i][1]}.mp3")
        tts.save(f"orig_name/{name}_{lang[i][0]}_{lang[i][1]}.mp3")


for voice in stream_elements.Voice:
   #print(voice)
   if voice == stream_elements.Voice.cmn_CN_Wavenet_D:
       break
   arr.append(f"{voice}.mp3")
   data = stream_elements.requestTTS('stanley', voice.value)
   with open(f"orig_name/{voice}.mp3", '+wb') as file:
        file.write(data)

for name in arr:
     for j in range(5):
          name_mp3 = AudioSegment.from_file(f"orig_name/{name}")
          name_mp3 = name_mp3 - name_mp3.dBFS - 23
          silence = AudioSegment.silent(duration=1000)
          name_mp3 = silence + name_mp3 + silence
          rand1 = random.randint(1, 10)
          rand2 = random.randint(1, 5)
          background = AudioSegment.from_file(f"new_back/background{rand1}_{rand2}.mp3")
          name_mp3.overlay(background).export(f"final_name/{name}_{j + 1}.mp3", format='mp3')
     