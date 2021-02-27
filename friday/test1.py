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
value = 0

def speak(audio):
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    friday.say("it")
    speak(Time)
    print(Time)

def command():
    with speech_recognition.Microphone() as mic:
        audio = friday_hearing.record(mic, duration = 3)
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
        elif "do you know about" in str:
            print(str[18:len(str)])
            speak('Here is my answer on google chrome')
            url=f"https://www.google.com/search?q={str[18:len(str)]}"
            webbrowser.get().open(url)

def conversation(str):
        if "hello" in str:
            speak("hello my boss, how can i help you")
        elif "time" in str:
            time()
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

if __name__ == "__main__":
    Friday_infor.openFriday()
    while True:
        voice_boss = command().lower()
        search(voice_boss)
        conversation(voice_boss)
        # if "hello" in voice_boss:
        #     speak("hello my boss, how can i help you")
        # elif "google" in voice_boss:
        #     speak("What should i search Boss")
        #     search=command().lower()
        #     url=f"https://www.google.com/search?q={search}"
        #     webbrowser.get().open(url)
        #     speak(f'Here is your {search} on google chrome')
        # elif "youtube" in voice_boss:
        #     speak("What should i search Boss")
        #     search=command().lower()
        #     url=f"https://www.youtube.com/search?q={search}"
        #     webbrowser.get().open(url)
        #     speak(f'Here is your {search} on youtube')
        # elif "time" in voice_boss:
        #     time()
        # elif "turn off" in voice_boss:
        #     value = 1
        #     speak("yes boss")
        # elif "friday" in voice_boss:
        #     value = 0
        # elif "open facebook" in voice_boss:
        #     speak("facebook is opening")  
        #     Browser('https://www.facebook.com/')
        # elif "music" in voice_boss:
        #     speak("Do you want to listen to music")
        #     speak("opening music on youtube")
        #     Browser('https://www.youtube.com/watch?v=leAlprToECY&list=PLfauYiLl00OpKReDoJbtrwKRIyOQiFH2a')
        # elif "watching film" in voice_boss:
        #     speak("Opening film on browser")
        #     Browser('http://www.phimmoizz.net')
        # elif "game" in voice_boss:
        #     speak("Opening garena")
        #     Browser('C:/Program Files (x86)/Garena/Garena/Garena.exe')
        # elif "photo" in voice_boss:
        #     speak("Opening photo on google chrome")
        #     Browser('https://photos.google.com')
        # elif "your name" in voice_boss:
        #     Friday_infor.Name()
        # elif "myself" in voice_boss:
        #     boss.infor_boss()
        # elif "contact" in voice_boss:
        #     boss.contact()
        # elif "do you know about" in voice_boss:
        #     print(voice_boss[18:len(voice_boss)])
        #     speak('Here is my answer on google chrome')
        #     url=f"https://www.google.com/search?q={voice_boss[18:len(voice_boss)]}"
        #     webbrowser.get().open(url)
        # elif "very good" in voice_boss:
        #     Friday_conversation.praise()
        # elif "goodbye" in voice_boss:
        #     speak("Have a nice day boss, goodbye")
        #     quit()
