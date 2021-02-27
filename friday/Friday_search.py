import speech_recognition 
import pyttsx3
import datetime
import webbrowser
import Friday_infor
import Friday_conversation
import boss

# Friday setting up to say 
friday = pyttsx3.init()
friday_hearing = speech_recognition.Recognizer()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)
rate = friday.getProperty('rate')   
friday.setProperty('rate', 200)    

def speak(audio):
    friday.say(audio)
    friday.runAndWait()

def command():
    with speech_recognition.Microphone() as mic:
        audio = friday_hearing.record(mic, duration = 4)
    try:
        voice_boss = friday_hearing.recognize_google(audio, language='en')
        print(voice_boss)
    except speech_recognition.UnknownValueError:
        voice_boss = ""
        print("...")
    return voice_boss

def Browser(link):
    url=f"{link}"
    webbrowser.get().open(url)

def search(str):
        if "google" in str:
            speak("What should i search Boss")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on google chrome')
        elif "youtube" in str:
            speak("What should i search Boss")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open facebook" in str:
            speak("facebook is opening")  
            Browser('https://www.facebook.com/')
        elif "music" in str:
            speak("Do you want to listen to music")
            speak("opening music on youtube")
            Browser('https://www.youtube.com/watch?v=leAlprToECY&list=PLfauYiLl00OpKReDoJbtrwKRIyOQiFH2a')
        elif "watching film" in str:
            speak("Opening film on browser")
            Browser('http://www.phimmoizz.net')
        elif "game" in str:
            speak("Opening garena")
            Browser('C:/Program Files (x86)/Garena/Garena/Garena.exe')
        elif "photo" in str:
            speak("Opening photo on google chrome")
            Browser('https://photos.google.com')
        elif "search" in str:
            print(str[7:len(str)])
            search = str[7:len(str)]
            speak(f'Here is {search} on google chrome')
            url=f"https://www.google.com/search?q={str[7:len(str)]}"
            webbrowser.get().open(url)


