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
from pygame import mixer
import urllib.request
import urllib.parse
import json
import bs4
import datetime
import os


class bcolors:
    blue = '\033[94m'
    ENDC = '\033[0m'



    # loop back to continue to listen for commands if unrecognizable speech is received



#ui isn't even ui, but make a ui that moves in the future
def ui():
    print(bcolors.blue + "            ********                        ********            ")
    print("        ****        ****                ****        ****        ")
    print("      **                **            **                **      ")
    print("     *                    *          *                    *     ")
    print("     *         *          *          *          *         *     ")
    print("     *                    *          *                    *     ")
    print("      **                **            **                **      ")
    print("        ****        ****                ****        ****        ")
    print("            ********                        ********            ")
    print("                          ************")
    print("                            ********")
    print("                              ****")
    print("                **                             **                    ")
    print("                  *****                   *****           ")
    print("                       *******************" + bcolors.ENDC)
ui()

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
        #print("I'm listening")
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        # listens for the user's input
        audio = r.listen(source)
        #print("analyzing...")
        #commented out for ui reasons

    try:
        command = r.recognize_google(audio).lower()
        #print("You said: " + command + "\n")
        #commented out for ui
        time.sleep(0)

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talk("your last command couldn't be heard")
        command = myCommand()

    return command


def eva(command):
    errors = ["I don't know what you mean", "Excuse me?", "Can you repeat that please?"]
    if "eva" in command:
        while 1 < 5:
            if "i'm a turtle" in command:
                talk("awkward...")
            elif "hello" in command:
                talk("Hello! I'm EVA. How can I help you?")
                time.sleep(3)
            elif "who are you" in command:
                talk("I am a virtual assitant created by ")
                time.sleep(3)
            elif "go to sleep" in command:
                talk("night night")
                time.sleep(2)
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

            elif "what is the weather" in command:
                city = "ottawa"
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=61db280dace1379f4c3921e839ce74f5&units=metric'.format(city)
                response = requests.get(url)
                data = response.json()
                #print(data)
                temp = data['main']['temp']
                round_temp = int(round(temp))
                talk('It is {} degrees celcius in {}'.format(round_temp, city))
                time.sleep(0)


            elif "eva turn off" in command:
                exit()

            elif "what is the time" in command:
                talk(datetime.datetime.now())



            else:
                error = random.choice(errors)
                talk(error)
                time.sleep(3)
    else:
        while 1 < 5:
            if "i'm a turtle" in command:
                talk("awkward...")
            elif "hello" in command:
                talk("Hello! I'm EVA. How can I help you?")
                time.sleep(3)
            elif "who are you" in command:
                talk("I am a virtual assitant created by ")
                time.sleep(3)
            elif "go to sleep" in command:
                talk("night night")
                time.sleep(2)
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

            elif "what is the weather" in command:
                city = "ottawa"
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=61db280dace1379f4c3921e839ce74f5&units=metric'.format(city)
                response = requests.get(url)
                data = response.json()
                #print(data)
                temp = data['main']['temp']
                round_temp = int(round(temp))
                talk('It is {} degrees celcius in {}'.format(round_temp, city))
                time.sleep(0)


            elif "eva turn off" in command:
                exit()

            elif "what is the time" in command:
                talk(datetime.datetime.now())



            else:
                error = random.choice(errors)
                talk(error)
                time.sleep(3)


        #talk("...EVA!,AWAKE AND READY TO GO")





# loop to continue executing multiple commands
while True:
    time.sleep(0)
    eva(myCommand())
