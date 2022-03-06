import vk_api
import random


class VkMemesProcessor:
    token = "7ad7c1c67ad7c1c67ad7c1c6e17aac43d077ad77ad7c1c618f395ea99beaf89c212f970"
    group_id = "-80799846"

    def __init__(self):
        self.attachment: str
        self.vk = vk_api.VkApi(token=self.token)
        self.vk._auth_token()


    def get_memes(self):
        randon_offset = random.randint(1, 1000)
        res = self.vk.method("wall.get", {"owner_id": self.group_id, "count": 1, "offset": randon_offset})
        return res
    
    def get_memes_id(self):
        while True:
            randon_offset = random.randint(1, 1000)
            res = self.vk.method("wall.get", {"owner_id": self.group_id, "count": 1, "offset": randon_offset})
            attachments = res.get("items", [{}])[0].get("attachments", [{}])
            attachment_type = attachments[0].get("type")
            if len(attachments) == 1 and attachment_type == "photo":
                return attachments[0]["photo"]["id"]
    
    def run(self):
        memes_id = self.get_memes_id()
        self.attachment = f"photo{self.group_id}_{memes_id}"




if __name__ == "__main__":
    res = VkMemesProcessor().get_memes_id()
    print(res)
