import speech_recognition as sr
import os
import webbrowser
from playsound import playsound
from gtts import gTTS
import time
from time import ctime
import random as rd

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            i = 1
            while 0.5 and i < 3:
                speak('Sorry I did not get that')
                voice_data = record_audio()
                response(voice_data)
                i += 1
            exit()
        except sr.RequestError:
            speak('Sorry, my speech service is down')
    return voice_data


# def shoeDepartment(question):
#     words = question.split()
#     new = list()
#     for n in words:
#         if n == "don't":
#             new.append(n)
#             print(new)
#         if n == 'size':
#             new.append(n)
#             print(new)
#     if new == ["don't", 'size']:
#         speak('I can help you measure your feet size')


def response(voice_data):
    if "i don't know about my size"in voice_data:
        question = "i don't know about my size"
        words = question.split()
        new = list()
        for n in words:
            if n == "don't":
                new.append(n)
                print(new)
            if n == 'size':
                new.append(n)
                print(new)
        if new == ["don't", 'size']:
            print('I can help you measure your feet size')

    if 'what is your name' in voice_data:
        speak('my name is Dillon and I am a sale associate')
    if 'hello' in voice_data:
        speak('hello Dillon awesome man')
    if ' are you a dog?' in voice_data:
        speak('yes and I love Nam')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'you are stupid' in voice_data:
        speak('I love you Dillon, you are my favorite master')
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('here is the location of ' + location)
    if 'hi' in voice_data:
        filename = record_audio(
            'Dillon, can you please tell me what is the file name?')
        filename = filename+'.txt'
        mode = record_audio('do u want to 1 or 2 your file?')
        if mode == '1':

            file = open(filename, 'w+')
            for i in range(1):
                file.write("you are so so so genius \r\n")
            file.close()
            file = open(filename, 'r')
            a = list(file)
            a = [n.rstrip() for n in a]
            for i in a:
                speak(i)
            print(a)
            file.close()
        if mode == '2':
            fileCollection = {}
            all_files = os.listdir('/Users/dillonvu/voiceRecognition/')
            print(len(all_files))
        exit()
    if 'exit' in voice_data:
        exit()


def speak(text):
    print(text)
    tts = gTTS(text=text, lang='en')
    filename = 'sound.mp3'
    tts.save(filename)
    playsound(filename)


time.sleep(1)

speak(' how Can I help you today?')

while 1:
    voice_data = record_audio()
    response(voice_data)
