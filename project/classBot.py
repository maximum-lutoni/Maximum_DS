from concurrent.futures import process
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from Modules.course import CourseProcessor
from Modules.wiki import WikipediaProcessor
from Modules.weather import WeatherProcessor
from Modules.memes import VKMemesProcessor
from Modules.news import NewsProcessor


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
    
    