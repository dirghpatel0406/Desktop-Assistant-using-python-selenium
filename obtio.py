import keyboard
import pyttsx3
from pyttsx3 import driver 
import speech_recognition as sr
import datetime 
import webbrowser
import os
import pyaudio
from pygame import mixer
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from pynput.mouse import Button,Controller
mouse = Controller()
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Obito Activated")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
            
def search(input):
    url="https://www.youtube.com/"
    driver = webdriver.Chrome("...")
    driver.get(url)
    driver.find_element_by_name("search_query").send_keys(input)
    driver.find_element_by_id("search-icon-legacy").click()
    a= input.replace(" ","+")
    driver.get(f"https://www.youtube.com/results?search_query={a}")
    sleep(1)
    mouse.position = (266,355)
    sleep(0.5)
    mouse.click(Button.left,1)
    sleep(0.5)
    mouse.position = (628, 480)
    sleep(8)
    mouse.click(Button.left,2)
    sleep(20) 

ending = ['close','exit','stop']

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak("Opening youtube!!")
            while True:
                speak("What you Would like to search sir?")
                sleep(0.5)
                quary3 = takeCommand().lower()
                sleep(0.5)
                if quary3 in ending:
                    speak("exiting from the youtube")
                    break
                a = quary3
                speak(f"searching {a} on youtube")  
                search(a)

        elif 'open google' in query:
            speak("Opening google!!")
            speak("What you want to search on google")
            quary4 = takeCommand().lower()
            brave_path = r"..."
            webbrowser.register('brave',None,webbrowser.BackgroundBrowser(brave_path))
            webbrowser.get('brave').open_new_tab('www.google.com')
            mouse.position = (598, 277)
            sleep(0.5)
            mouse.click(Button.left,2)
        
        elif 'open whatsapp' in query:
            speak("Opening whatsapp!")
            codePath = "..."
            os.startfile(codePath)
                
        elif 'play music' in query:
            
            music_dir = '...'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening visual studio code!")
            codePath = "..."
            os.startfile(codePath)

        elif 'email to name' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "yourmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Something Went Wrong! sorry sir") 

            except:
                speak("Error  Error  Error  Error  Error  Error  Error  Error  Error")
        
        elif query in ending:
            speak("Have A good bye Sir, See you soon!")
            break
