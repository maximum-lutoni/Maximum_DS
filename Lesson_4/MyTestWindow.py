from tkinter import *            # импортируем все элементы tkinter


root = Tk()                      # создаем элемент класса Tk
root.title("Моё приложение")     # задаем заголовок окна
root.geometry("500x500+500+100") # "width x heigth + X + Y"

lab = Label(root, text="0", bg = "blue", fg = "green", font = "16") # виджет с текстом
lab.place(x=200, y=100)                                             # размещение виджета

img = PhotoImage(file="logo.png") 
logo = Label(root, image=img)     #виджет с фото
logo.place(x=0, y=0)

#lab["text"] = "Замена"
lab["fg"] = "white"

def changeLabel():                  
    count = int(lab['text'])  # берем значение атрибута 'text' и переводим его в int
    count += 1                # count = count + 1
    lab['text'] = count       # возвращаем нужное значение

def changelabel():
    lab['text'] = int(lab['text']) + 1 #короткая запись от Вовы

btn = Button(text = "Кнопка",       # виджет кнопки
            background="#555",      # фон
            foreground="#ccc",      # цвет текста
            font = "16",            # размер текста
            command = changeLabel   # действия при нажатии кнопки
            )

btn.place(x=200, y=200)

root.mainloop() #создание и отрисовка окна