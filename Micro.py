# dob of Micro is [14-02-22]
from multiprocessing.spawn import _main
from threading import main_thread
from pip import main


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")    


    speak ("I am Micro. Please tell me how may I help you Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
 
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
  wishMe()
while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'micro open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'micro open google' in query:
            webbrowser.open("google.com")

        elif 'micro open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'micro open github' in query:
            webbrowser.open("github.com")


        elif 'micro play akinator' in query:
            webbrowser.open("akinator.com")

            
        elif 'micro open puretoons' in query:
            webbrowser.open("puretoons.com")

            
        elif 'micro open flipkart' in query:
            webbrowser.open("flipkart.com")

            
        elif 'micro open translator' in query:
            webbrowser.open("google translate.com")



        elif 'micro play music' in query:
          n = random.randint(0,4)
          print(n)

          music_dir = 'E:\Documents\Music'
          song = os.listdir(music_dir)
          print(song)

          os.startfile(os.path.join(music_dir,song[n]))


        elif 'micro what is time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strtime}")


        elif 'micro open code' in query:
            codePath = "C:\\Users\\cpmee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'micro open command' in query:
            codePath = "%windir%\\system32\\cmd.exe"
            os.startfile(codePath)


        

        elif 'hello'==query:
            speak('hello Sir')

        elif 'hai' == query:
            speak('hi Sir')

        elif 'what is your name' == query:
            speak('my name is Micro')

        elif 'what is your age' == query:
            speak('my age is less than 1 month')

        elif 'which is your country' == query:
            speak('My country is india')
            
        elif 'who is your boss' == query:
            speak('You are my Boss')
            
        elif 'who make you' == query:
            speak('I am Made by Sahil kumar')
            
        elif 'who is sahil kumar' == query:
            speak('Sahil Kumar are Coder , he was Make me')

        elif 'how are you' in query:
            speak('i am fine Sir , Thank you')
            
        elif 'whats up' in query:
            speak('Nothing Sir')
            
        elif 'tell me something' in query:
            speak('Hello sir, my name is Micro')
            
        elif 'ok' in query:
            speak('ok sir')
            
        elif 'thank you' in query:
            speak('your most welcome sir')
            
        elif 'goodbye' in query:
            speak('goodbye sir')
            
        elif 'good night' in query:
            speak('good night')
            
        elif 'how can you help me' in query:
            speak('what help you need sir')
            
        elif 'happy birthday' in query:
            speak('Sorry , Today is not my birthday')
            
        elif 'can you help me' in query:
            speak('Yes sir , this is my work')
            
        elif 'do you know a joke' in query:
            speak('no sir')
            
        elif 'do you like people' in query:
            speak('Yes sir , i like people')
            
        elif 'you are smart' in query:
            speak('thank you sir')
            
        elif 'i want the answer now' in query:
            speak('Sorry sir')
            
        elif 'are you human' in query:
            speak('no sir')
            
        elif 'are you a robot' in query:
            speak('i am artificial chatbot not a robot')
            
        elif 'what is your mother name' in query:
            speak('i have not mother')
            
        elif 'what is your father name' in query:
            speak('i have not my father')
            
        elif 'where do you live' in query:
            speak('i live in rajasthan , india')
        elif 'what is your data of birth' in query:
            speak('my date of birth is 14 2 2022')




        
