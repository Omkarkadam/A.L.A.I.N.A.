import datetime
from playsound import playsound
from pyttsx3 import speak
import speech_recognition as sr
speak("Enter Hour:")
alarmHour = int(input("Enter Hour:"))
speak("Enter Minutes:")
alarmMin = int(input("Enter Minutes:"))
speak("Enter am/pm:")
alarmAm = input("am / pm:")
    
    
r = sr.Recognizer()
with sr.Microphone() as source:
    r.pause_threshold = 1
    r.energy_threshold = 494
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)


if alarmAm=='pm':
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        speak("Wake up omkar Sir Alarm is on...")
        playsound("aliana.mp3")
        break
