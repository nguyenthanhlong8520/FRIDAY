# import ctypes
# import time
# import keyboard
# dll = ctypes.WinDLL('user32.dll')
# dll.LockWorkStation()
# time.sleep(2)
# keyboard.send('enter')
# keyboard.send('l,o,n,g,8,5,2,0')
# keyboard.send('enter')


# # elif "write a note" in query:
# #             speak("What should i write, sir")
# #             note = takeCommand()
# #             file = open('jarvis.txt', 'w')
# #             speak("Sir, Should i include date and time")
# #             snfm = takeCommand()
# #             if 'yes' in snfm or 'sure' in snfm:
# #                 strTime = datetime.datetime.now().strftime("% H:% M:% S")
# #                 file.write(strTime)
# #                 file.write(" :- ")
# #                 file.write(note)
# #             else:
# #                 file.write(note)
         
# #         elif "show note" in query:
# #             speak("Showing Notes")
# #             file = open("jarvis.txt", "r") 
# #             print(file.read())
# #             speak(file.read(6))