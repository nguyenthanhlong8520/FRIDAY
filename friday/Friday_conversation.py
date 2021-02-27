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
    # friday.say("it")
    speak(f"The time is {Time}")
    # speak(Time)
    print(Time)

def praise():   
    friday.setProperty('rate', 150)     
    friday.say("oh boss, thanks")
    friday.setProperty('rate', 200) 
    friday.runAndWait()

def conversation(str):
        if "hello" in str:
            speak("hello my boss, how can i help you")   
        elif "time" in str:
            time()
        elif "friday" in str:
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

