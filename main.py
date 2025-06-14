import pyttsx3
import speech_recognition as sr
import webbrowser

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
    

    if "open youtube" in user.lower():
        webbrowser.open("https://youtube.com")
    if "open google" in user.lower():
        webbrowser.open("https://google.com")
    
    