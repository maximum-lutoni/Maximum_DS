import requests

class NewsProcessor:
    token = "api_key"   #Добаить свой ключ
    country = "ru"

    def __init__(self):
        response: str

    # получаем json ответ новостей
    def _get_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country={self.country}&apiKey={self.token}"
        res = requests.get(url)
        return res.json()["articles"][:10]

    # разбираем полученный ответ 
    def _format_response(self,news):
        res = ""
        for post in news:
            res += f"{post['title']}\n Источник: {post['url']}\n\n"
        return res
    
    # фунция для запуска
    def run(self):
        news = self._get_news()
        self.response = self._format_response(news)
