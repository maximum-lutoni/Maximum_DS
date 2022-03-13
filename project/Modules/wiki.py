import wikipedia
class WikipediaProcessor():

    def __init__(self,*args):
        self.article = args[0]
        message:str
        wikipedia.set_lang("ru")

    def _get_response(self):
        if not self.article:
            return "Запрос пустой"
        try:
            return wikipedia.summary(self.article)
        except wikipedia.exceptions.PageError:
            return "Не удалось обнаружить иформацию по запросу"
    
    def run(self):
        self.message = self._get_response()

def get_wikipedia_summary(article):
    wikipedia.set_lang("ru")
    if not article:
        return "Запрос пустой"
    try:
        return wikipedia.summary(article)
    except wikipedia.exceptions.PageError:
        return "Не удалось обнаружить иформацию по запросу"
