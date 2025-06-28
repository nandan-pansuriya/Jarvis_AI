import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import keyboard
import pyautogui
import datetime
import psutil
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import screen_brightness_control as sbc


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

def search_command(command):
    query = command.replace("search","").split()[0]
    keyboard.press_and_release("ctrl+l")
    keyboard.write(query)
    pyautogui.sleep(0.5)
    keyboard.press_and_release("enter")

def play_song_command(command):
    os.system("start spotify")
    pyautogui.sleep(5)
    query = command.replace("play song","").strip()
    keyboard.press_and_release("ctrl+k")
    pyautogui.sleep(1)
    keyboard.write(query)
    pyautogui.sleep(2)
    keyboard.press_and_release("enter")

def is_wifi_enable() :
    interfaces = psutil.net_if_stats()
    
    if 'Wi-Fi' in interfaces :
        return interfaces['Wi-Fi'].isup
    else :
        return False

devices = AudioUtilities.GetSpeakers()  
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
def set_volume(level): 
    volume.SetMasterVolumeLevelScalar(level / 100, None)

def get_current_volume():
    current = volume.GetMasterVolumeLevelScalar()  
    return round(current * 100)




hour = datetime.datetime.now().hour

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


    elif "switch window" in user :
        pyautogui.hotkey('alt','tab')   
    
    elif "Focus on search bar" in user:
        pyautogui.hotkey('ctrl','l')  

    elif "new tab" in user :
        pyautogui.hotkey('ctrl','n')   

    elif "close all tab" in user :
        pyautogui.hotkey('ctrl','shift','w')
    
    elif "close window" in user or "close current window" in user :
        keyboard.send("alt+tab")

    elif "zoom in" in user :
        pyautogui.hotkey('ctrl','+')  

    elif "zoom out" in user :
        pyautogui.hotkey('ctrl','-')  
    
    elif "open quick settings" in user :
        pyautogui.hotkey('win','a') 

    elif "on wi-fi" in user :
        if is_wifi_enable() :
            speak("wi-fi is already enabled")
        else :
            pyautogui.hotkey('win','a')
            pyautogui.sleep(0.1)
            pyautogui.press('enter')

    elif "off wi-fi" in user:
        if is_wifi_enable() :
            pyautogui.hotkey('win','a')
            pyautogui.sleep(0.1)
            pyautogui.press('enter')
        else :
            speak("wi-fi is already disabled")

    elif "on bluetooth" in user or "off bluetooth" in user :
        pyautogui.hotkey('win','a')
        pyautogui.sleep(0.1)
        pyautogui.press('right')
        pyautogui.sleep(0.1)
        pyautogui.press('enter')
        pyautogui.sleep(0.1)
        pyautogui.hotkey('win','a')

    elif "set volume to" in user :
        query = user.split()[3]
        set_volume(int(query))

    elif "increase volume" in user :
        current_volume = get_current_volume()
        new_volume = min(current_volume + 10, 100)  # increase by 10%, max is 100
        set_volume(new_volume)

    elif "decrease volume" in user :
        current_volume = get_current_volume()
        new_volume = min(current_volume - 10, 100)  # increase by 10%, max is 100
        set_volume(new_volume)

    elif "set brightness to" in user :
        query = user.split()[3]
        sbc.set_brightness(query)
    
    elif "increase brightness" in user :
        sbc.set_brightness('+10')

    elif "decrease brightness" in user :
        sbc.set_brightness('-10')

    elif "click" in user:
        pyautogui.click()
        speak("Mouse clicked.")

    elif "enter" in user :
        keyboard.press('enter')

    elif "search" in user:
        search_command(user)
    
    elif "play song" in user:
        play_song_command(user)


    elif "exit" in user :
        speak("Shutting down.")
        exit()

