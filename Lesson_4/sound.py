import os                             # работа с Операционной системой.
from pygame import mixer              # работа с mp3 файлами
from gtts import gTTS                 # инструменты google для озвучивания текста
import time                           # работа со временем


my_string = "Какой-то текст"


tts=gTTS(text=my_string, lang='ru')   # озвучиваем текст и записываем в переменную
tts.save("my.mp3")                    # сохраняем mp3 файл


mixer.init()                          # инициализируем модуль mixer

mixer.music.load("my.mp3")            # загружаем файл
mixer.music.play()                    # запускаем
time.sleep(2)                         # ждем 2 секунды

mixer.quit()
os.remove("my.mp3")                   # удаляем файл
