import pyttsx4
import speech_recognition as sr
import os
import subprocess

engine = pyttsx4.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    speak("Hello! I'm your startup assistant. How can I help you today?")

def start_desired_programs():
    # Replace these with the programs you want to start
    programs_to_start = [
        "notepad.exe",  # Example: Notepad
        "chrome.exe"    # Example: Chrome
    ]

    for program in programs_to_start:
        os.system(f"start {program}")

def start_program_as_admin(program):
    try:
        subprocess.run(['runas', '/user:Administrator', program], check=True)
        print(f"Started {program} as administrator.")
    except subprocess.CalledProcessError:
        print(f"Failed to start {program} as administrator.")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            print(f"User said: {user_input}")
            return user_input.lower()
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear anything.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            speak("I'm having trouble accessing the recognition service.")
            return None



# todoSpeak()