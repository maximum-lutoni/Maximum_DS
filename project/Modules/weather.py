from venv import create
import requests

class WeatherProcessor:
    weather_token = "71b4baa1e65fc3391caf943a3fd02f05"
    api_url= "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    def __init__(self, city):
        self.city = city
        response: str
        self.lat : str
        self.lon : str

    def _get_wether_info(self):
        self._get_city_info()
        response = requests.get(self.api_url.format(lat= self.lat,api_key= self.weather_token, lon = self.lon))
        return response.json()
    
    def _get_city_info(self):
        city_url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=2&appid={api_key}"
        response = requests.get(city_url.format(city_name = self.city ,api_key= self.weather_token))
        data = response.json()
        self.lat = data[0].get("lat")
        self.lon = data[0].get("lon")
        if self.lat is None:
            self.response = "Город не найден"
            return
        

        
    
    def _create_response(self):
        data = self._get_wether_info()
        main = data.get("main")
        
        temp = main["temp"] - 273.15
        feels_like = main["feels_like"] - 273.15
        pressure = main["pressure"]
        humidity = main["humidity"]
        self.response = f"Температура в {self.city.title()} {round(temp)}°C, ощущается как {round(feels_like)}°C"\
            f"\nДавление: {pressure} мм рт. ст."\
            f"\nВлажность: {humidity}%"


    def run(self):
        self._create_response()
        