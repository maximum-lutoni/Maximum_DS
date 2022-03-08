from venv import create
import requests

#Класс выводящий погоду по городу.

class WeatherProcessor:
    weather_token = "api_key"   #Добаить свой ключ
    api_url= "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    # инициализируем класс по городу
    def __init__(self, city):
        # инициализируем нужные поля
        self.city = city    # создаем поле city
        response: str       # response
        self.lat : str      # lat
        self.lon : str      # lon
    
    # получаем ответ по api_url
    def _get_wether_info(self):
        self._get_city_info()
        response = requests.get(self.api_url.format(lat= self.lat,api_key= self.weather_token, lon = self.lon))
        return response.json()
    
    # получаем координаты по городу  
    def _get_city_info(self):
        city_url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=2&appid={api_key}"
        response = requests.get(city_url.format(city_name = self.city ,api_key= self.weather_token))
        data = response.json()
        self.lat = data[0].get("lat")   
        self.lon = data[0].get("lon")
        if self.lat is None:
            self.response = "Город не найден"
            return
    
    # создаем response 
    def _create_response(self):
        data = self._get_wether_info()
        main = data.get("main")          # переходим по ключу "main"
        
        # извлекаем нужные для нас данные
        temp = main["temp"] - 273.15
        feels_like = main["feels_like"] - 273.15
        pressure = main["pressure"]
        humidity = main["humidity"]
        # заносим строку для вывода в response
        self.response = f"Температура в {self.city.title()} {round(temp)}°C, ощущается как {round(feels_like)}°C"\
            f"\nДавление: {pressure} мм рт. ст."\
            f"\nВлажность: {humidity}%"

    # метод для запуска процессора
    def run(self):
        self._create_response()
        
