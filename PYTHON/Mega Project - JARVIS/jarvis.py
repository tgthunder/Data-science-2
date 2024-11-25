
import pyttsx3
import datetime
import speech_recognition as sr 
import time
import wikipedia
import webbrowser
import os
import random
import json
import pywhatkit

from urllib import response
from urllib.request import urlopen
url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hours=int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good morning ")

    elif hours>12 and hours<18:
        speak("Good afternoon ")
        
    elif hours>18 and hours<20:

        speak("Good evining ")
        


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")  #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
    
    
if __name__=="__main__":
    speak("Hello I am jarvis")
    
    wishme()

    speak("What can I do for you sir ")
    while True:
    
        query=takeCommand().lower()
    # logic for executing task for query
        if 'wikipedia' in query:
            speak("searching wekipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("sir acoording to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'music' in query:
            music_dir='C:\\Users\\reliance\\Music\\music_dir'
            songs=os.listdir(music_dir)
            print(songs)

            os.startfile(os.path.join(music_dir,random.choice(songs)))
            
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is {strTime}")

        elif 'open code' in query:
            codepath='"C:\\Users\\reliance\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)

        elif 'where' in query:
            speak(f"sir You are in {data.get('city')} {data.get('region')}")

         

        elif 'who' in query:
            speak("My name is jarvis and I am a Robot")

        elif 'sudarshan' in query:
            speak("Sudarshan is computer engineer")
            speak(" He is very good boy ")

        elif 'stop' in query:
            speak("Thank You so much sir ")
            hour=datetime.datetime.now().hour
            if hour>20:
                speak("Good night sir")
                speak("Have a great night sir")
            else:
                speak("have a good day sir")
            break
        elif 'My name' in  query:
            speak("Hello sir what can I do for you")

        elif 'good' in query:
            speak("Thank you sir")

        elif 'whatsapp' in query:
            speak("Ok sir")
            pywhatkit.sendwhatmsg('+918446359940',"Message from Jarvis sir",21,11)
         


        
        
        else:
            speak("sorry sir I am not able to understand what You are saying ")

        