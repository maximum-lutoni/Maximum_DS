import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, "lxml")



#<Valute ID="R01010">
def getCourse(id):
    return xml.find("valute",{'id': id }).value.text
    

if __name__ == "__main__":
    print(response.url)
    print(getCourse("R01235"), "рублей за 1 доллар")
    print(getCourse("R01239"), "рублей за 1 евро")
    print(getCourse("R01375"), "рублей за 10 юаней")
