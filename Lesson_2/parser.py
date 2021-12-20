import requests
from bs4 import BeautifulSoup

city = "vladivostok"
country = "russia"
url = "https://world-weather.ru/pogoda/"
response = requests.get(url + country + "/" + city)

html = BeautifulSoup(response.content, "lxml")

print(response)

#Ответ 1xx -- загрузка
#Ответ 2xx -- означает что все работает
#Ответ 3xx -- перенаправление запроса
#Ответ 4xx -- ошибка на стороне пользователя
#Ответ 5xx -- ошибка на стороне сайта

def temp():
    #<div id="weather-now-number">0<span>°</span></div>

    return html.find("div", {'id': "weather-now-number"}).text
    #return html.select("div#weather-now-number")[0].text

def condition():
    #<span title="Облачно" id="weather-now-icon" class="wi n400 tooltip"></span>
    
    return html.find("span", {"id":"weather-now-icon"})['title']

def humidity():
    return html.select("#weather-now-description  dd")[2].text # id - #

def time_of_day():
    time_now = html.find("div",{"class":"weather-now-info"}).p.b.text # class - .
    #time_now = html.select('div.weather-now-info')[0].p.b.text
    time_now = time_now[:5]
    time_now = int(time_now[:2])*60 + int(time_now[-2:])

    sunrise = 10*60
    sunset = 17*60

    if time_now >= sunset or time_now < sunrise:
        return "\U0001F31A"
    if time_now >= sunrise and time_now < sunset:
        return "\U0001F31E"

def main():
    temp_value = temp()
    wether_condition =condition()
    time_day = time_of_day()
    print(time_day, temp_value, wether_condition, "Влажность "+ humidity())
    

main()
