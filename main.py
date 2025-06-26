import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import keyboard
import pyautogui
import datetime

engine = pyttsx3.init()

def speak(text):  
    print(text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio,language="en-in")
            print(f"You said : {command}")
            return command
        except Exception as e:
            print(f"Error : {e}")
            print("Say again ....")
            return "Error"

def greet_user(hour) :
        
    if hour < 12 :
        speak("Good morning, Sir ")
    elif hour <18 :
        speak("Good afternoon, Sir")
    else:
        speak("Good evening, Sir")


hour = datetime.datetime.now().hour

# speak("Hello, my name is Jarvis. I am your personal assistant. How can I help you today?")
greet_user(hour)

speak("I am jarvis AI, How can i help you ...")

while True:
    
    user = take_command().lower()

    if user == "error" :
        continue

    if "hello" in user:
        speak("Hello sir, How can i help you ...")

    if "open youtube" in user :
        speak("opening Youtube ...")
        # webbrowser.open("https://youtube.com")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/YouTube.lnk")
    
    elif "open github" in user :
        speak("opening Github ...")
        # webbrowser.open("https;//github.com")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/github.lnk")

    elif "open classroom" in user :
        speak("opening Classroom ...")
        # webbrowser.open("https://classroom.google.com")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/Google Classroom.lnk")

    elif "open vs code" in user :
        speak("opening VS code ...")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk")

    elif "open chrome" in user :
        speak("opening Chrome ...")
        os.system("start chrome")        

    elif "open google" in user :
        speak("opening Google ...")
        webbrowser.open("https://google.com")

    elif "open linkedin" in user :
        speak("opening Linkedin ...")
        # webbrowser.open("https://linkedin.com")
        os.system("start linkedin:")

    elif "open whatsapp" in user :
        speak("opening WhatsApp ...")
        # webbrowser.open("https://whatsapp.com")
        os.system("start whatsapp:")

    elif "open notepad" in user :
        speak("opening Notepad ...")
        os.system("start notepad")

    elif "open chatgpt" in user :
        speak("opening ChatGPT ...")
        webbrowser.open("https://chatgpt.com")

    elif "open file explorer" in user :
        speak("opening File Explorer ...")
        os.system("start explorer")

    elif "open command prompt"  in user :
        speak("opening Command Prompt ...")  
        os.system("start cmd")

    elif "open spotify" in user :
        speak("opening Spotify ...")
        os.system("start spotify")

    elif "open start menu" in user :
        pyautogui.press('win')




    # if "minimize window" in user :
    #     pyautogui.hotkey('win','down')
    
    # elif "maximize window" in user :
    #     pyautogui.hotkey('win','up')


    if "switch window" in user :
        pyautogui.hotkey('alt','tab')  

    elif "enter" in user :
        keyboard.press('enter') 
    
    elif "Focus on search bar" in user:
        pyautogui.hotkey('ctrl','l')  

    elif "new tab" in user :
        pyautogui.hotkey('ctrl','n')   

    elif "close tab" or "close current tab" in user :
        pyautogui.hotkey('ctrl','w')
    
    elif "close all tab" in user :
        pyautogui.hotkey('ctrl','shift','w')
    
    elif "close window" or "close current window" in user :
        keyboard.send("alt+tab")


    if "exit" in user :
        speak("Shutting down.")
        exit()
