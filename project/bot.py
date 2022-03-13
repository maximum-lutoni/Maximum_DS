from concurrent.futures import process
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from Modules.course import CourseProcessor
from Modules.wiki import WikipediaProcessor
from Modules.weather import WeatherProcessor
from Modules.memes import VKMemesProcessor
from Modules.news import NewsProcessor

def main():
    TOKEN = "4dca71364da2c42822a9db6f75598e419d63c65998d68618ba6a4c178acc9c6b90f9e2870c94c21621816"   #записать свой ключ

    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    hello_message = "Привет, я бот, я могу выполнять следующие команды:\n"\
                    "-к - курс валют\n"\
                    "-с <запрос>  cправка о чем-то\n"\
                    "-п <город>  погода в городе\n"\
                    "-м отправлять случайный мем\n"\
                    "-н сводка новостей"
    

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            random_id = random.randint(1,100000000)


            if msg[0:2] == "-к":
                processor = CourseProcessor()
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=processor.response)

            if msg[0:2] == "-с":
                processor = WikipediaProcessor(msg[2:])
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=processor.response)                
            
            if msg[0:2] == "-п":
                processor = WeatherProcessor(msg[2:].strip())
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=processor.response)
            
            if msg[0:2] == "-м":
                processor = VKMemesProcessor()
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, attachment=processor.attachment)
            
            if msg[0:2] == "-н":
                processor = NewsProcessor()
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=processor.response)
            



            else:
                vk.messages.send(user_id = user_id, random_id = random_id, message = hello_message)
main()
