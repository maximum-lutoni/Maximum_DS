#wikipedia.set_lang("ru")

#print(wikipedia.summary("россия"))
#print(wikipedia.search("россия"))

#russia = wikipedia.page("россия")

#print(russia.title)       #заголовок
#print(russia.url)         #url
#print(russia.content)     #вся страницв
#print(russia.links)       #ccылки

#wikipedia.summary("россия")  #первый абзац

import wikipedia

def get_wikipedia_summary(article):
    wikipedia.set_lang("ru")
    if not article:
        return "Запрос пустой"
    try:
        return wikipedia.summary(article)
    except wikipedia.exceptions.PageError:
        return "Не удалось обнаружить иформацию по запросу"
