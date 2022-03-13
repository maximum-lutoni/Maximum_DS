import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from Modules.course import CourseProcessor
from Modules.wiki import WikipediaProcessor
from Modules.weather import WeatherProcessor
from Modules.memes import VKMemesProcessor
from Modules.news import NewsProcessor
import argparse


class Bot:
    def __init__(self,token):
        vk_session = vk_api.VkApi(token=token)
        self.vk = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
        self.hello_message = "Привет, я бот Федор, я могу выполнять следующие команды:\n"\
                        "-к - курс валют\n"\
                        "-с <запрос>  cправка о чем-то\n"\
                        "-п <город>  погода в городе\n"\
                        "-м отправлять случайный мем\n"\
                        "-н сводка новостей"
        
        self.handlers={
            "-к": CourseProcessor,
            "-c": WikipediaProcessor,
            "-п": WeatherProcessor,
            "-м": VKMemesProcessor,
            "-н": NewsProcessor
        }
    def _get_response(self, handler, query):
        if handler is None:
            return {"message":self.hello_message}
        
        processor = handler(query)
        processor.run()  
        return {atr: getattr(processor,atr) for atr in ("message","attachment") if  getattr(processor, atr, None)}

    def _handle_message(self,msg):
        handler = self.handlers.get(msg[0:2])
        query = msg[2:].strip()
        return self._get_response(handler,query)

    def run(self):
        while True:
            try:   
                for event in self.longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        msg = event.text.lower()
                        random_id = random.randint(1,100000000)
                        params = {"user_id":event.user_id ,"random_id":random_id, **self._handle_message(msg)}
                        self.vk.messages.send(**params)
            except Exception:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Конфигурация бота")
    parser.add_argument('--token','-t',type=str, help="Токен для бота")
    args = parser.parse_args()
    bot = Bot(args.token)
    bot.run()