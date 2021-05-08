#pip install googletrans==4.0.0-rc1
#convert text from one language to another using google translate and python
import pyttsx3
from googletrans import Translator, LANGUAGES
from googletrans.models import Translated
from pyttsx3 import speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
lang = list(LANGUAGES.values())
speak("Welcome to ALIANA Translate")
speak("Please Enter Your Text in english:\n")
input_text = input("Please Enter Your Text in english:\n")
speak("Please enter output language name (ex.-hindi,gujarati,japanese:\n" )
out_lang = input("Please enter output language name (ex.-hindi,gujarati,japanese:\n ").lower()
if out_lang not in lang:
    speak("Sorry This Language is not available to translate")
    print("Sorry This Language is not available to translate")
else:
    translator = Translator()
    translated = translator.translate(text=input_text, src="english",dest=out_lang)
    translated = str(translated).split(", ")
    converted = translated[2]
    pro = translated[3]
    speak(converted)
    print(converted)
    speak(pro)
    print(pro)
    