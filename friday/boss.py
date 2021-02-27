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

def infor_boss():   
    speak("You are my boss")

def contact():
    friday.setProperty('rate', 140)     
    friday.say("email: nguyenthanhlong8520@gmail.com")
    friday.say("phone number: 0384768818")
    friday.setProperty('rate', 200) 
    friday.runAndWait()


