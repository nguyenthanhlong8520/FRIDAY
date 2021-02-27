import speech_recognition 
import pyttsx3
import datetime

# Friday setting up to say 
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)
rate = friday.getProperty('rate')   
friday.setProperty('rate', 200)     

def speak(audio):
    friday.say(audio)
    friday.runAndWait()

def Name():   
    friday.setProperty('rate', 150)     
    friday.say("I'm friday")
    friday.setProperty('rate', 200) 
    friday.runAndWait()

def openFriday():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <= 10:
        speak("Good morning, Boss")
    elif hour >= 11 and hour <= 12:
        speak("Good noon, Boss")
    elif hour >= 13 and hour <= 18:
        speak("Good afternoon, Boss")
    elif hour >= 19 and hour <= 21:
        speak("Good evening, Boss")
    else:
        speak("Good night, Boss")
    speak("How can i help you")

