import speech_recognition as sr 

def get_audio():

    if(not True):
        rObject = sr.Recognizer()
        audio = ''
        with sr.Microphone() as source:
            print("Speak...")
            audio = rObject.listen(source, phrase_time_limit = 30) 
        print("Stop.")
        try:
            text = rObject.recognize_google(audio, language ='en-US')
            print("You : "+text)
            return str(text).lower()
        except:
            return ("Could not understand your audio, PLease try again !")
    else:
        return input("speak :")
    
 