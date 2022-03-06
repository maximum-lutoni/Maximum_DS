from tokenize import group
import vk_api
import random

class VKMemesProcessor:
    token = "api_key"   #Добаить свой ключ
    group_id = "-80799846"

    def __init__(self):
        self.attachment : str
        self.vk = vk_api.VkApi(token=self.token)
        self.vk._auth_token()
    
    def get_memes(self):
        random_offset = random.randint(1,1000)
        res = self.vk.method("wall.get",{"owner_id":self.group_id,"count":1,"offset":random_offset})
        return res
    
    def get_memes_id(self):
        while True:
            random_offset = random.randint(1,1000)
            res = self.vk.method("wall.get",{"owner_id":self.group_id,"count":1,"offset":random_offset})
            attachment = res.get("items",[{}])[0].get("attachments",[{}])
            attachment_type = attachment[0].get("type")
            if len(attachment) == 1 and attachment_type == "photo":
                return attachment[0]["photo"]["id"]
    
    def run(self):
        memes_id = self.get_memes_id()
        self.attachment = f'photo{self.group_id}_{memes_id}'



if __name__ == "__main__":
    res = VKMemesProcessor().get_memes()
    print(res["items"][0]["attachments"][0]["photo"]["id"])
