import requests

class NewsProcessor:
    token = "d9513d2246f740ddb7b86858fd548650"
    country = "ru"

    def __init__(self):
        pass

    def get_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country={self.country}&apiKey={self.token}"
        res = requests.get(url)
        return res.json()["articles"][:10]


    def format_response(self,news):
        res = ""
        for post in news:
            res += f"{post['title']}\n Источник: {post['url']}\n\n"
        return res

 #   def format_response_2(self,news):
 #       return "\n\n".join(f"{news["title"]}\n Источник: {news['url']}")


    def run(self):
        news = self.get_news()
        self.response = self.format_response(news)