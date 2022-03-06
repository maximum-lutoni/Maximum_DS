from concurrent.futures import process
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from Modules.course import getCourse
from Modules.wiki import get_wikipedia_summary
from Modules.weather import WeatherProcessor
from Modules.memes import VKMemesProcessor

def main():
    TOKEN = "4dca71364da2c42822a9db6f75598e419d63c65998d68618ba6a4c178acc9c6b90f9e2870c94c21621816"

    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    hello_message = "Привет, я бот, я могу выполнять следующие команды:\n"\
                    "-к - курс валют\n"\
                    "-с <запрос>  cправка о чем-то\n"\
                    "-п <город>  погода в городе\n"\
                    "-м отправлять случайный мем"
    

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            random_id = random.randint(1,100000000)


            if msg[0:2] == "-к":
                response = "{0} рублей за 1 доллар \n {1} рублей за 1 евро \n {2} рублей за 10 юаней\n  {3} рублей за 1 фунт"
                response = response.format(getCourse("R01235"),getCourse("R01239"),getCourse("R01375"),getCourse("R01035"))
                vk.messages.send(user_id = user_id, random_id = random_id, message = response)
            if msg[0:2] == "-c":
                response = get_wikipedia_summary(msg[2:])
                vk.messages.send(user_id = user_id, random_id = random_id, message = response)
            #добавить модуль погоды
            if msg[0:2] == "-п":
                processor = WeatherProcessor(msg[2:].strip())
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=processor.response)
            
            if msg[0:2] == "-м":
                processor = VKMemesProcessor()
                processor.run()
                vk.messages.send(user_id=event.user_id, random_id=random_id, attachment=processor.attachment)




            else:
                vk.messages.send(user_id = user_id, random_id = random_id, message = hello_message)
main()
