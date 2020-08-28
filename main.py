import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!!")
    
    else:
        speak("Good Evening!!!")

    speak("Hello I am Jarvis. Please tell me how may I help you")

def takeCommand():
    # it takes input from microphone and convert into string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('lapuidea771@gmail.com', 'jairam4567')
    server.sendmail('lapuidea771@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    # logic for executing task  based on Query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipediqa")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
        
        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")
        
        elif 'open github' in query:
            webbrowser.get(chrome_path).open("github.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\sagar\\Desktop\\JARVIS\\music_dir'
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))

        elif 'the time' in query:
            x = datetime.datetime.now()
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Boss! The time is {strTime}")

        elif 'visual studio' in query:
            codePath = "C:\\Users\\sagar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'pycharm' in query:
            pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(pyPath)

        elif 'email to sagar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sgrgyanchandani@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry Boss!! I am not able to send this e-mail at this moment")

        elif 'quit' in query:
            speak("Quitting Now.. Thanks for your time...Bosss")
            exit()
