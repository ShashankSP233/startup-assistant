import pyttsx4
import speech_recognition as sr
import os
import subprocess
from  cboxfun import *

if __name__ == "__main__":
    greet_user()
    
    while True:
        user_input = listen()
        
        if user_input:
            if "start" in user_input:
                if "admin" in user_input:
                   speak("can you specify what to start?")
                   user_input = listen()
                   start_program_as_admin(f'{user_input}.exe')
                else: 
                    start_desired_programs()
                speak("I've started the desired programs.")
            elif any(word in user_input for word in ["close", "exit"]):
                speak("Goodbye!")
                break
            else:
                speak("I'm not sure how to help with that. Could you please try something else?")