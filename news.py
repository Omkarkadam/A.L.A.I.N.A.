import requests
import json
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=4f3c2ac75b414ff6a39cceaf31534df0'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')

def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=in&apiKey=4f3c2ac75b414ff6a39cceaf31534df0'

if __name__ == '__main__':
    speak_news()
