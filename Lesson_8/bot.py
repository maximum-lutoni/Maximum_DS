import vk_api
import time
from parser import*

token = "4dca71364da2c42822a9db6f75598e419d63c65998d68618ba6a4c178acc9c6b90f9e2870c94c21621816"

vk = vk_api.VkApi(token= token)
vk._auth_token()


while True:
    messages = vk.method("messages.getConversations", {"count": 20,"filter": "unanswered"})

    if messages["count"] > 0:
        id = messages['items'][0]['last_message']['from_id'] #id
        text = messages['items'][0]['last_message']['text'] #text
        message_id = messages['items'][0]['last_message']["id"]
        print(text)
        if text.lower() == "курс":
            vk.method("messages.send", {"peer_id": id,"random_id": message_id,"message": getCourse("R01235")})
        else:
            vk.method("messages.send", {"peer_id": id,"random_id": message_id,"message": "Неизвестная команда"})
        
        