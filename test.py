import speech_recognition as sr 
import playsound
from gtts import gTTS 
import os
import threading
 
import google.generativeai as palm
palm.configure(api_key='AIzaSyB7HZBYvn2bMJXaoddUn57cNnPW-jzNghM')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def get_bard_message(query):
    completion = palm.generate_text(
    model=model,
    prompt=query,
    temperature=0,
    max_output_tokens=800,
)
    return completion.result

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
    def stopped(self):
        return self._stop_event.is_set()
class new():
    def assistant_speaks(self,text=None):
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

def get_audio():
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        audio = rObject.listen(source, phrase_time_limit = 30) 
    print("Stop.")
    try:
        text = rObject.recognize_google(audio, language ='en-US')
        print("You : ", text)
        return str(text).lower()
    except:
        return ("Could not understand your audio, PLease try again !")
 

temp=new()
Thread1=StoppableThread(target=temp.assistant_speaks)
while True:
    text=get_audio()
    
    if "hey jarvis" in text:
        if "prepare for coding" in text:
            temp.assistant_speaks(text="do you want to open all development tools")
            decision=get_audio()
            if "yes" in decision:
                os.startfile("C:\\Users\\sakth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                os.startfile("C:\\Users\\sakth\\AppData\\Local\\JetBrains\\IntelliJ IDEA Community Edition 2023.2.3\\bin\\idea64.exe")
            else:
                temp.assistant_speaks(text="provide name of the software to open")
                software=get_audio()
        elif "prepare for gaming" in text:
            os.startfile("C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\Win32\\EpicGamesLauncher.exe")
        else:
            text.replace("hey jarvis","")
            text=get_bard_message(text)
            f1=open('file.txt', 'w')
            f1.write(text)
            f1.close()
            
            # assistant_speaks(text)
            Thread1.start()
    elif "stop playback" in text:
        Thread1.stop()