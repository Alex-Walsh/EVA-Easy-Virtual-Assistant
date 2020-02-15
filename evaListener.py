import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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
        print("you said:")
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
    errors = ["I don't know what you mean", "Excuse me?", "Can you repeat that please?"]

    if "eva" or "EVA" or "Eva" in command:
        os.system('python3 test1.py')
        exit()

    else:
        os.system('python3 evaListener.py')
        exit()
# loop to continue executing multiple commands
while True:
    time.sleep(0)
    eva(myCommand())
