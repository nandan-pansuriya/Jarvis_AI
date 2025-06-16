import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import keyboard
import pyautogui

engine = pyttsx3.init()

def speak(text):  
    print(text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"You said : {command}")
            return command
        except Exception as e:
            print(f"Error : {e}")
            print("Say again ....")
            return "Error"



speak("Hello, I am jarvis AI...")

while True:
    
    user = take_command()
    if "hello" in user.lower():
        speak("Hello sir, How can i help you ...")

    if "open youtube" in user.lower():
        # webbrowser.open("https://youtube.com")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/YouTube.lnk")
        speak("opening Youtube ...")
    
    elif "open github" in user.lower():
        # webbrowser.open("https;//github.com")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/github.lnk")
        speak("opening Github ...")

    elif "open classroom" in user.lower():
        # webbrowser.open("https://classroom.google.com")
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome Apps/Google Classroom.lnk")
        speak("opening Classroom ...")

    elif "open vs code" in user.lower():
        os.startfile("C:/Users/pansu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk")
        speak("opening VS code ...")

    elif "open chrome" in user.lower():
        os.system("start chrome")        
        speak("opening Chrome ...")

    elif "open google" in user.lower():
        webbrowser.open("https://google.com")
        speak("opening Google ...")

    elif "open linkedin" in user.lower():
        # webbrowser.open("https://linkedin.com")
        os.system("start linkedin:")
        speak("opening Linkedin ...")

    elif "open whatsapp" in user.lower():
        # webbrowser.open("https://whatsapp.com")
        os.system("start whatsapp:")
        speak("opening WhatsApp ...")

    elif "open notepad" in user.lower():
        os.system("start notepad")
        speak("opening Notepad ...")

    elif "open chatgpt" in user.lower():
        webbrowser.open("https://chatgpt.com")
        speak("opening ChatGPT ...")

    elif "open file explorer" in user.lower():
        os.system("start explorer")
        speak("opening File Explorer ...")

    elif "open command prompt"  in user.lower():
        os.system("start cmd")
        speak("opening Command Prompt ...")  

    
    
    

    if "exit" in user.lower():
        speak("Shutting down.")
        exit()

    