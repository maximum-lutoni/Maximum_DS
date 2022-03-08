import requests

class NewsProcessor:
    token = "api_key"   #Добаить свой ключ
    country = "ru"

    def __init__(self):
        response: str

    # получаем json ответ новостей
    def get_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country={self.country}&apiKey={self.token}"
        res = requests.get(url)
        return res.json()["articles"][:10]

    # разбираем полученный ответ 
    def format_response(self,news):
        res = ""
        for post in news:
            res += f"{post['title']}\n Источник: {post['url']}\n\n"
        return res
    
    # фунция для запуска
    def run(self):
        news = self.get_news()
        self.response = self.format_response(news)
