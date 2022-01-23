import requests
from bs4 import BeautifulSoup


def temp(html):
    return html.find("div",{"id":"weather-now-number"}).text
    
def condition(html):
    return html.find("span",{"id":"weather-now-icon"})['title']

def wind_speed(html):
	return html.select("#weather-now-description dd span")

def term_value(html):
	return html.select("#weather-now-description dd")[1].text

def humidity(html):
	return html.select("#weather-now-description dd")[2].text

def time_in_min(time):
    return int(time[:2]) * 60 + int(time[3:])

def time_of_day(html):
    time_now = html.find("div",{"class":"weather-now-info"}).p.b.text
    time_now = time_now[:5]
    time_now = int(time_now[:2]) * 60 + int(time_now[3:])
    
    sun = html.find("ul",{"class":"sun"}).li.text
    sunrise = sun[8:13]
    sunrise = time_in_min(sunrise)
    sunset = sun[21:26]
    sunset = time_in_min(sunset)

    if time_now >= sunset or time_now < sunrise:
        return "\U0001F31A"
    elif time_now >= sunrise and time_now < sunset:
        return "\U0001F31E"


    
def main():
    country = input("Введите страну: ")
    city = input("Введите город: ")
    url = "https://world-weather.ru/pogoda/"
    response = requests.get(url + country + "/" + city)
    
    html = BeautifulSoup(response.content, "lxml")
    try:
        temp_value = temp(html)
        weather_condition = condition(html)
        time_day=time_of_day(html)
        wind = wind_speed(html)
        wind = "Ветер " + wind[0].text + " м/с" + wind[1].text
        term = "Давление " + term_value(html)
        
        
    except AttributeError:
        print("Город не найден")
    else:
        print(time_day, temp_value, weather_condition,wind,term, "Влажность " + humidity(html))

    main()


main()