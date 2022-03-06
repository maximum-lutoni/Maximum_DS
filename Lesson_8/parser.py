import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()                 #С помощью библиотеки datetime получаем дату сегодня.
today = today.strftime("%d/%m/%Y")       #Форматируем дату под нужный нам вывод: дд/мм/гггг

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, "lxml")

def getCourse(id):
    return xml.find("valute",{'id': id }).value.text
    


