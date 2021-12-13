import spacy
import requests

nlp = spacy.load("fr_core_news_md")

def getweather1(location):
    url = 'http://api.weatherapi.com/v1/current.json?key=48b046708754403f8a2185826211210&q={}'
    response = requests.get(url.format(location)).json()

    display_list = {}
    display_list['API_Name'] = 'Weatherapi.com'
    display_list['city_name'] = location

    if 'error' in response:
        display_list['error'] = response['error']['message']
    else:
        display_list['temp'] = response['current']['temp_c']
        display_list['weather'] = response['current']['condition']['text']
        display_list['icon'] = response['current']['condition']['icon']
    return display_list


def chatbot():

    doc = nlp("Je veux la Meteo de Marseille")

    for entity in doc.ents:
        entity._tag
#         print(getweather1(entity.text))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chatbot()

