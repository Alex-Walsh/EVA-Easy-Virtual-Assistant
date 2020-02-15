import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from gtts import gTTS
import speech_recognition as sr
import re
import time
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import requests
import urllib.request
import urllib.parse
import json
import bs4
import datetime
import cv2
import numpy as np

def talk(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang="en-uk")
        text_to_speech.save("audio.mp3")
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()

def myCommand():
    "listens for commands"
    # Initialize the recognizer
    # The primary purpose of a Recognizer instance is, of course, to recognize speech.
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I'm listening")
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        # listens for the user's input
        audio = r.listen(source)
        print("analyzing...")

    try:
        command = r.recognize_google(audio).lower()
        print(command + "\n")
        time.sleep(0)

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print("Your last command couldn't be heard")
        command = myCommand()

    return command


def eva(command):
    errors = ["I don't know what you mean", "Excuse me?", "Can you repeat that please?", "sorry I didn't catch that", "oops I wasn't paying attention"]

    if "i'm a turtle" in command:
        talk("awkward...")
    elif "hello" in command:
        talk("Hello! I'm EVA. How can I help you?")
        time.sleep(0)
        os.system('python3 evaListener.py')
        exit()

    elif "nevermind" in command:
        time.sleep(0)
        os.system('python3 evaListener.py')
        exit()
    elif "who are you" in command:
        talk("I am a virtual assisant created by alex")
        time.sleep(0)
        os.system('python3 evaListener.py')
        exit()

    elif "go to sleep" in command:
        talk("night night")
        time.sleep(0)
        exit()
        #all weather commands
    elif "weather in" in command:
        city = command.split("in", 1)[1]
        #openweathermap API

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=61db280dace1379f4c3921e839ce74f5&units=metric'.format(city)
        response = requests.get(url)
        data = response.json()
        #print(data)
        temp = data['main']['temp']
        round_temp = int(round(temp))
        talk('It is {} degrees celcius in {}'.format(round_temp, city))
        time.sleep(0)
        os.system('python3 evaListener.py')
        exit()
    elif "what is the weather" or "what's the weather" in command:
        city = "ottawa"
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=61db280dace1379f4c3921e839ce74f5&units=metric'.format(city)
        response = requests.get(url)
        data = response.json()
        #print(data)
        temp = data['main']['temp']
        round_temp = int(round(temp))
        talk('It is {} degrees celcius in {}'.format(round_temp, city))
        time.sleep(0)
        os.system('python3 evaListener.py')
        exit()



    elif "eva turn off" in command:
        exit()

    elif "what is the time" in command:
        talk(datetime.datetime.now())
        os.system('python3 evaListener.py')
        exit()

    elif "what is your favourite color" or "what is your favourite colour" in command:
        colors = ['green','blue','red']
        color = random.choice(colors)
        talk("what ever yours is, but I prefer", color)
        os.system('python3 evaListener.py')
        exit()


    else:
        error = random.choice(errors)
        talk(error)
        time.sleep(0)



#talk("Hello, please allow me three seconds to warm up before you tell me your command")

# loop to continue executing multiple commands
while True:
    time.sleep(4)
    eva(myCommand())
