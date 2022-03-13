from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from pygame import mixer
from gtts import gTTS
import time

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req" : today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text

def voice_course():
    
    mp3_name = "audio.mp3"                                             # имя файла
    valutes = [                                                        # создаем список строк для воспроизведения
        "За 1 доллар дают {} рублей".format(getCourse("R01235")[:-2]),
        "За 1 евро дают {} рублей".format(getCourse("R01239")[:-2])
    ]

    for valute in valutes:                    # проходим по каждому жлементу списка
                   
        tts = gTTS(text=valute, lang='ru')
        tts.save(mp3_name)

        mixer.init()
        mixer.music.load(mp3_name)
        mixer.music.play()
        time.sleep(6)

        mixer.quit()
        #os.remove(mp3_name)




window = Tk()
window.title("Курс валют")
window.geometry("400x350+300+300")

#img = PhotoImage(file='logo.png')
#logo = Label(window, image=img)
#logo.place(x=0, y=0)

lab = Label(window, text = "Курс валют \n Maximum банк", font="Arial 22")
lab.place(y=25, x=150)

# .replace(x, y) - метод заменяет в строке все вхождения x на y 
course_info = Label(window, text= "Курс на:" + today.replace("/","."), fg="black", font="Arial 18")
course_info.place(y=150, x=90)

usd_course = Label(window, text = "$ " + getCourse("R01235"), font = "Arial 16")
usd_course.place(y=190, x=100)
eur_course = Label(window, text = "€ " + getCourse("R01239"), font = "Arial 16")
eur_course.place(y=230, x=100)

voice_btn = Button(text= "Озвучить",
            background="#555",
            foreground="#ccc",
            font = "Arial 16",
            command=voice_course)

voice_btn.place(x=250, y=270)

window.mainloop()