#Работа с файлами
#
#r - чтение
#w - запись
#a - добавление
#r+ - запись и чтение

import os
from pygame import mixer
from gtts import gTTS
import time

my_file = open("file.txt",'w')
my_file.write("Какой-то текст")
my_file.close()

my_file = open("file.txt", "r")
my_text = my_file.read()
print(my_text)
my_file.close()

my_file = open("file.txt", "r")
my_string = my_file.read()
my_file.close()

mp3_name = "audio.mp3"

mixer.init()

tts=gTTS(text=my_string, lang='ru')

tts.save(mp3_name)
mixer.music.load(mp3_name)
mixer.music.play()
time.sleep(5)
mixer.quit()
os.remove(mp3_name) 