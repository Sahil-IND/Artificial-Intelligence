import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good afternoon Sir")

    else:
        speak("Good evening Sir ")

    speak("Hello I am Zid. please tell me how Can I Help You")

def takeCommand():
    

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        var_skjezdyl = r
        var_skjezdyl.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query=takeCommand().lower()

        #logics for executing tasks based on query
        if 'wikipedia' in query:
         speak('searching in Wikipedia...')
         query=query.replace("Wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)

        elif 'open youtube' in query:
             webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play Music' in query:
            music_dir ='C:\\Users\\Default\\Music'
            songs = os.listdir()
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'quit' in query:
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:
            codepath = "C:\\Users\\sahil\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'telegram' in query:
            codepath = "C:\\Users\\sahil\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codepath)

        
        elif 'chrome' in query:
            codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)

