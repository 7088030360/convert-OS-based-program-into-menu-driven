import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("//_-_-_-_-_-_-_-_-WELCOME HERE-_-_-_-_-_-_-_-_-//\n")
speak("Welcome dear,how can i help you")
print("Here some system based menu")

while True:

    print("1. open notepad\n 2. open chrome\n 3.open command prompt\n 4. open you tube\n 5. open linkedin\n 6.open amazon\n 7.open gmail")
    speak("please choose your option")
    text=input()
    if text == "notepad" or text=="Notepad":
        speak("Opening notepad")
        os.system("notepad")
        wait = input(" plzz press Enter to continue")


    elif text== "chrome":
        speak("Opening Chrome")
        os.system("MicrosoftEdge chrome.com")
        wait = input(" plzz press Enter to continue")

    elif text == "command prompt":
        speak("Opening command prompt")
        os.system("cmd")
        wait = input(" plzz press Enter to continue")

    elif text == "youtube" or text=="Youtube":
        speak("Opening youtube")
        os.system("MicrosoftEdge youtube.com")
        wait = input(" plzz press Enter to continue")


    elif text == "Linkedin" or text=="linkedin":
        speak("Open linkedin")
        os.system("MicrosoftEdge linkedin.com")
        wait = input(" plzz press Enter to continue")

    elif text == "Amazon" or text=="amazon":
        speak("open amazon")
        os.system("MicrosoftEdge amazon.com")
        wait=input(" plzz press Enter to continue")

    elif text=="gmail" or text=="Gmail":
        speak("open g-mail box")
        os.system("MicrosoftEdge gmail.com")
        wait = input(" plzz press Enter to continue")

    elif text == "exit":
        speak("quitting, Thank you dear. I would like to help you again")
        break
        exit()
    else:
        print("wrong input")