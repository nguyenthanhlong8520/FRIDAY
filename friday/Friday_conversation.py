import speech_recognition 
import pyttsx3
import datetime
import webbrowser
import Friday_infor
import Friday_conversation
import boss

# Friday setting up to say 
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)
rate = friday.getProperty('rate')   
friday.setProperty('rate', 200)         

def speak(audio):
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(f"The time is {Time}")
    print(Time)

def praise():   
    friday.setProperty('rate', 150)     
    friday.say("oh boss, thanks")
    friday.setProperty('rate', 200) 
    friday.runAndWait()

def conversation(str):
        if "hello" in str:
            speak("hello my boss, how can i help you")   
        elif 'how are you' in str:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'i am fine' in str or "crazy" in str:
            speak("It's good to know that your fine")
        elif "time" in str:
            time()
        elif "hi friday" in str:
            speak("I'm listening")   
        elif "your name" in str:
            Friday_infor.Name()
        elif "myself" in str:
            boss.infor_boss()
        elif "contact" in str:
            boss.contact()
        elif "very good" in str:
            Friday_conversation.praise()
        elif "goodbye" in str:
            speak("Have a nice day boss, goodbye")
            quit()

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

