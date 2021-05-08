from math import degrees
import random
import datetime
from urllib.request import urlopen
from PyDictionary.core import PyDictionary
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import os
import time
import datetime
from googletrans import Translator
from requests import get
import pywhatkit
import smtplib
import sys
import pyautogui

import google #import gcloud services enable language.googleapis.com # Google Cloud Natural Language API
import googletrans
from PyDictionary import PyDictionary as Diction
from bs4 import BeautifulSoup
from time import sleep
import quotes
import playsound
import keyboard
import requests
import json
import feedparser
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search



import wolframalpha

from tkinter import *
# importing YouTube module
from pytube import YouTube
# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("400x350")
# setting the title of the GUI
root.title("Youtube video downloader application")

app = wolframalpha.Client("7LQE88-H5EHJ2APH7")



    




def computational_intelligence(question):
    try:
        client = wolframalpha.Client("7LQE88-H5EHJ2APH7")
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[4].id)






def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        a = "Good morning my Master", "Good morning master", "Hello Omkar Good Morning", "O, Good morning respected sir", "O, good morning Omkar", "Wow! Welcome back Omkar sir"
        speak(random.choice(a))
    elif hour >= 12 and hour < 18:
        b = "Good Afternoon Omkar", "Good Afternoon sir", "Hello Omkar Good Afternoon", "O, Good Afternoon sir", "O, good Afternoon Omkar", "Wow! Welcome back Omkar sir"
        speak(random.choice(b))
    else:

        c = "Good Evening Omkar", "Good Evening sir", "Hello Omkar Good Evening", "O, Good Evening sir", "O, good Evening Omkar", "Wow! Welcome back Omkar sir"
        speak(random.choice(c))


wishMe()
wel = "So, how can i help you sir!", "How can i help", "Give me a command Sir", "Online and ready sir", "What can i do for you", "Please give me a command Sir"
speak(random.choice(wel))


def CloseAPPS():
    speak("Ok Sir , Wait A second!")

    if 'close youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

    elif 'close chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

    elif 'close telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")



    elif 'close cmd' in query:
            os.system("TASKKILL /F /im cmd.exe")
    
    elif 'pdf' in query:
            os.system("TASKKILL /F /im Acrobat.exe")

    elif 'notepad' in query:
            os.system("TASKKILL /F /im notepad.exe")
            
    speak("Your Command Has Been Succesfully Completed!")






def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("omkar.kadam5@gmail.com", "OmkarKadam@19978")
    server.sendmail("omkar.kadam5@gmail.com", to, content)
    server.close()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except:

        # print(e)

        print('Say that again please...')
        return 'None'
    
    return query

def takeHindi():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='hi')
        speak(f'User said: {query}\n')

    except:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query

def SpeedTest():
    import speedtest
    speak("Checking Speed......")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    if 'uploading' in query:
        speak(f"The uploading speed is {correctUpload}mbps")
    elif 'downloading' in query:
        speak(f"The downloading speed is {correctDown}mbps")
    else:
        speak(f"The downloading speed is {correctDown}mbps and the Uploading Speed is {correctUpload}mbps")


def Tran():
    speak("Tell me a line")
    line = takeHindi()
    translate = Translator()
    result = translate.translate(line)
    Text = result.text
    speak(f"The translation for this line is:"+Text)
   
def dicto():
    dicto("Activated Dictionary!")
    dicto("Tell Me The prob!")
    prob = takeCommand()
    if 'meaning' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of", "")
        prob = prob.replace("meaning of", "")
        result = Diction.meaning(prob)
        speak(f"The Meaning For {prob} is {result}")
    elif 'synonym' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of", "")
        prob = prob.replace("synonym of", "")
        result = Diction.synonym(prob)
        speak(f"The Synonym For {prob} is {result}")

    elif 'antonym' in prob:
        prob = prob.replace("what is the", "")
        prob = prob.replace("jarvis", "")
        prob = prob.replace("of", "")
        prob = prob.replace("antonym of", "")
        result = Diction.antonym(prob)
        speak(f"The Antonym For {prob} is {result}")
        speak("Exited Dictionary!")
    
 


if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        print(query)

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)


        elif"open adobe" in query or "acrobat" in query or "pdf" in query:
            bpath = "D:\\acrobat\\acrobat\\Acrobat\\Acrobat.exe"
            os.startfile(bpath)

        elif"open cmd" in query or "command prompt" in query:
            bpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(bpath)

        elif"open telegram" in query or "telegram" in query:
            bpath = "D:\\Telegram Desktop\\Telegram.exe"
            os.startfile(bpath)

        # ip address

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        #covid-19 notifer
        
        elif "covid-19 notifier" in query:
            
            import COVID19Py
            covid19 = COVID19Py.COVID19(data_source= 'jhu')
            latest = covid19.getLatest()
            from pynotifier import Notification
            Notification(
                title ="Today covid19 News Updates.",
                description = str(latest),
                duration = 30,  # Duration in seconds
            ).send()

        #covid-19 data
        
        elif "covid-19 data" in query or "covid-19 deta" in query:
            '''
            This is a Coronavirus Tracker program written by Omkar Kadam.
            You have to connect to internet and the run this program.
            If the program will run succesfully, it will show the name of a file and its location.
            In that file, all the data about different countries like no. of cases, deaths etc will be written in formatted way.
            Please try running this program on desktop.
            '''


            import requests
            import json

            import json
            import os
            import speech_recognition



            try:
                my_data=requests.get("https://api.covid19api.com/summary")

            except:
                print("Please connect to Internet and try again.")

            else:
                
                datastr=my_data.text

                data=json.loads(datastr)

                Global=data["Global"]
                Countries=data["Countries"]
                Date=data["Date"]
                date=Date.replace(Date[-1],"")
                date_list=date.split("T")
                data_date=date_list[0]
                data_time=date_list[1]

                filename="Coronavirus_cases_data.txt"
                write_data=""
                s_no=0
                write_data+=("This data is last updated at - "+"\nDate - "+data_date+"\nTime - "+data_time+"\n\n\n")
                write_data+=("Total Cases Worldwide -\n"+"Confirmed - "+str(Global['TotalConfirmed'])+"\n"+"Recovered - "+str(Global['TotalRecovered'])+"\n"+"Deaths - "+str(Global['TotalDeaths'])+"\n\n")
                write_data+=("\nThese the cases countrywise - \n\n")
                for c in Countries:
                    s_no+=1
                    spaces=(len(str(s_no))*" ")+"  "
                    write_data+=str(s_no)+". Country - "+str(c['Country'])+"\n"+spaces+"Confirmed - "+str(c['TotalConfirmed'])+"\n"+spaces+"Recovered - "+str(c['TotalRecovered'])+"\n"+spaces+"Deaths - "+str(c['TotalDeaths'])+"\n\n"

                with open(filename,"w") as f_obj:
                    f_obj.write(write_data)
                    speak(f"Your file '{filename}' is created/updated at '{os.getcwd()}'.")

        elif "speed test" in query:
            SpeedTest()


        # System information 
        elif "system info" in query or 'systeminfo' in query:
            import platform
            speak("Operating System type is:")
            speak(platform.system())  # e.g. Windows, Linux, Darwin
            speak("Operating system architecture type is:")
            speak(platform.architecture())  # e.g. 64-bit
            speak("System machine type")
            speak(platform.machine())  # e.g. x86_64
            speak("System name is:")
            speak(platform.node())  # Hostname
            speak("System processsor type is:")
            speak(platform.processor())  # e.g. i386

        # volume up,down,mute
        elif 'volume up' in query or "increase volume" in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query or "decrease volume" in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press("volumemute")

        if 'wikipedia' in query or "search on wikipedia" in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences=2)

                speak("so, wikipedia says")
                speak(results)

            except:
                speak("Not available on wikipedia")

        if 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))

            break

       
        elif 'how are you' in query:
            f ='fine sir', 'fine Omkar sir', 'fine what about you', 'fine, just doing my business', 'fine, waiting for your command sir'
            speak(random.choice(f))    
            break

           
        elif 'what is my age' in query:
            speak("As per looking your google account my calculation says your age lies between 22-25 years please correct me if I'm wrong")
            break

        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = takeCommand().lower()
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={x}")

        elif 'what is time' in query or 'time' in query:
           strTime = datetime.datetime.now().strftime("%I:%M %p")   
           speak(f"Sir, the time is {strTime}")

        elif 'open web browser' in query or 'open a new tab of browser' in query or 'open a web browser' in query:

            webbrowser.open("www.google.com")

        elif 'open facebook' in query or 'open fb' in query or 'fb' in query or 'fb' in query:
            webbrowser.open("www.facebook.com")

        elif 'open stackoverflow' in query or 'stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'what is your name' in query:
            speak('My name is Aliana. And Aliana stands for ALL Language Processing  Artificial Intelligence Neural Networks Augmentation JUST A RATHER VERY INTELLIGENT SYSTEM develped by Rohan Kelshikar and Omkar Kadam.')
       

        #elif 'search' in query:
            #query = query.replace("search", "")
            #webbrowser.open(f"https://www.google.com/search?q={query}")
           


        elif 'send email' in query or "email" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "omkar.kadam5@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry omkar sir,I am not able to send this email")

        elif 'joke' in query or 'i am bored' in query or "i'm bored" in query:
            speak("Omkar sir when i am here let me fresh up your mind!!")
            while(True):

                speak(pyjokes.get_joke())

        elif "activate mod" in query:
            from pywikihow import search_wikihow
            speak("How to do mod is activated please tell me what you want to know")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:

                os.system('shutdown -s')
            else:
                speak("ok sir")

        elif 'restart' in query or 're start' in query:
            speak("Do you really want to restart the system sir?")
            ch = takeCommand()
            if "yes" in ch:

                os.system('shutdown /r /t 1')
            else:
                speak("ok sir")

        elif "hibernate" in query or "sleep" in query:
            speak("Do you really want to hibernate the system sir?")
            ch = takeCommand()
            if "yes" in ch:

                os.system("shutdown / h")
            else:
                speak("ok sir")
            
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            speak("Do you really want to log off the system sir?")
            ch = takeCommand()
            if "yes" in ch:

                os.system(["shutdown", "/l"])
            else:
                speak("ok sir")
            
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('aliana.txt', 'w')

         
            file.write(note)
         
        elif "show note" in query or "show me notes" in query or "show me my notes" in query or "show me my note" in query:
            speak("Showing Notes")
            file = open("aliana.txt", "r")
            speak("So sir what you wrote in note is:-")
            speak(file.read())

        elif "play music" in query:
            speak("type the song name!")
            import ytmusic
           
        
            
        elif 'who are you' in query or "give me your introduction" in query:
            speak("Wait, i am introducing myself. My name is Aliana, I am an Assistant made by python progarmming, i can do many works like playing music, opening programs, opening youtube, searching on web and many more")
        elif "who am i" in query:
            jh = "if you are speaking then, definately you are a human", "You are Omkar", "You are a human", "I cant identify peoples with their vocies, may be you are Omkar or anybody with relation of Omkar"
            speak(random.choice(jh))
        elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day ahead!")
            sys.exit()

        elif 'location' in query or 'what is my location' in query:
            res = requests.get('https://ipinfo.io/')
            data = res.json()

            city = data['city']

            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]
            speak("Your latitude is:")
            speak(latitude)
            speak("Your Longitude is:")
            speak(longitude)
            speak("Your city is")
            speak(city)

        elif 'dictionary' in query:
            speak("Enter word to search")
            SearchWord = takeCommand()

            try:
                myDict = PyDictionary(SearchWord)
                speak("The meaning are:")
                speak(myDict.getMeanings())
                speak("The synonym are:")
                speak(myDict.getSynonyms())
                speak("The antonymm are:")
                speak(myDict.getAntonyms())
            except:
                print("Not Found")

        elif 'news' in query:
            
                url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=42ff6f17844d41e4aeab2fde4b21e948'
                open_page = requests.get(url).json()
                artic = open_page['articles']
                results = []
                for i in artic:
                    print(results.append(i['title']))

                for i in range (0,10):
                    print(i+1, results[i])
                    speak(results[i])

        elif 'search' in query:
            import wikipedia as googleScrape
            query = query.replace("Aliana","")
            query = query.replace("google serach"," ")
            query = query.replace("google", "")
            speak("This is what I found on the web")

            try:
                pywhatkit.search(query)
                result = googleScrape.summary(query, 3)
                speak(result)
            except:
                speak("No speakable data available")
            
            
        elif 'torrent' in query:
            from torrent import torrent
            
        elif 'quit' in query:
            exit()
       

        elif "calculate" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
            
        elif "what is" in query or "who is" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)

        elif 'good bye' in query:
            speak("good bye Have a great day ahead Omkar")
            exit()

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  

            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okay' or 'okey' in ans_take_from_user_how_are_you:
                speak('okay..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')

            elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
                ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
                speak(ex_exit)
                exit() 

            else:
                temp = query.replace(' ','+')
                g_url="https://www.google.com/search?q="    
                res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
                print(res_g)
                speak(res_g)
                webbrowser.open(g_url+temp)   

        elif "download youtube video" in query:
            speak("Ok omkar Sir!")

            def download():


    # using try and except to execute program without errors
             try:

                myVar.set("Downloading...")
                root.update()
                YouTube(link.get()).streams.first().download()
                link.set("Video downloaded successfully")

             except Exception as e:

                myVar.set("Mistake")
                root.update()
                link.set("Enter correct link")

            # created the Label widget to welcome user
            Label(root, text="Welcome to youtube\nDownloader Application", font="Consolas 15 bold").pack()
            # declaring StringVar type variable
            myVar = StringVar()
            # setting the default text to myVar
            myVar.set("Enter the link below")
            # created the Entry widget to ask user to enter the url
            Entry(root, textvariable=myVar, width=40).pack(pady=10)
            # declaring StringVar type variable
            link = StringVar()
            # created the Entry widget to get the link
            Entry(root, textvariable=link, width=40).pack(pady=10)
            # created and called the download function to download video
            Button(root, text="Download video", command=download).pack()
            # running the mainloop
            root.mainloop()
            speak("Omkar Sir The video is been downloaded sucessfully")  
            
        elif "screenshot" in query or "take a screenshot" in query:
            im1 = pyautogui.screenshot()
            im1.save("C:\\Users\\Administrator\\Desktop\\alaiana\\screen1.png")
        
        elif "translate" in query or "translate word" in query:
            
            Tran()

        elif "translation with text" in query:
            #pip install googletrans==4.0.0-rc1
            #convert text from one language to another using google translate and python

            import translatetext

        # Pdf Reader       
        elif "audiobook" in query:
            import pdfreader


        # Alarm code.
        elif 'alarm' in query:
         import alarm
         
        elif 'close youtube' in query:
            CloseAPPS()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close code' in query:
            CloseAPPS()

        elif 'close cmd' in query:
            CloseAPPS()

        elif 'close pdf' in query:
            CloseAPPS()

        elif 'close notepad' in query:
            CloseAPPS()
        
        elif 'repeat my word' in query:
            speak("Speak Sir!")
            jj = takeCommand()
            speak(f"You Said : {jj}")

        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("7LQE88-H5EHJ2APH7")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        #elif 'covid' in query:
            #import covid

        elif 'whatsapp' in query:
            from selenium import webdriver
           
            driver = webdriver.Chrome()
            driver.get("https://web.whatsapp.com/")
            driver.maximize_window()
            speak("Enter name or group name:")
            name = input(" ")
            speak("Enter message:")
            msg = input(" ")
            speak("Enter count:")
            count = int(input(" "))

            input("Enter anything after scan QR code")

            user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
            user.click()

            msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

            for index in range(count):
                msg_box.send_keys(msg)
                driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

            print("Success")


