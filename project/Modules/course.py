from urllib import response
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class CourseProcessor():
    
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    response = "{0} рублей за 1 доллар \n {1} рублей за 1 евро \n {2} рублей за 10 юаней\n  {3} рублей за 1 фунт"

    def __init__(self):
        today = datetime.today()
        today = today.strftime("%d/%m/%Y")

        payload = {"date_req": today}   
        response = requests.get(self.url, params=payload)
        self.xml = BeautifulSoup(response.content, "lxml")
        

    def _get_course(self,id):
        return self.xml.find("valute",{'id': id }).value.text

    def _create_response(self):
        self.response = self.response.format(self._get_course("R01235"),self._get_course("R01239"),self._get_course("R01375"),self._get_course("R01035"))

    def run(self):
        self._create_response()
        return self.response
        
    

if __name__ == "__main__":
    print(response.url)
    print(CourseProcessor._get_course("R01235"), "рублей за 1 доллар")
    print(CourseProcessor._get_course("R01239"), "рублей за 1 евро")
    print(CourseProcessor._get_course("R01375"), "рублей за 10 юаней")
