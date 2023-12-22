import pyttsx3
from gtts import gTTS 
import playsound
import os

speak=False
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def speak1(text=None):
    output=''
    if (text==None):
        output=open("file.txt").read()
    else:
        output=text
    print("PerSon : "+ output)
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    file = str("b")+".mp3 "
    toSpeak.save(file)
    print(file)
    try:
        playsound.playsound("./b.mp3", True) 
    except Exception as ex:
        print(ex)
    os.remove(file)