
import random

import a_vcontroll.listen as listen
import a_vcontroll.speak as speaker
import aimodel.palm as palm
import internatcheck.checkinternet as ic
import systemcontrol.applicationopenner as app
import playsound
import text.text as texts
# playsound.playsound("./audios/welcome.mp3")

while True:
    text=listen.get_audio()
    # if(not ic.check_internet()):
    #     speaker.speak(texts.offline[int(random.randint(0,(texts.offline.__len__())-1))])
    #     continue

    if "hey jarvis" in text:
        text=text.replace("hey jarvis", "")
        data=palm.extract_feature(text)
        if data["feature"]=="" or data["feature"]==None:
            speaker.speak("something went wrong")
            continue

        if data["feature"]=='openapp':
            app.open_application(data['appname'])

        if(data["feature"]=='birthdaywish'):
            print(text)
            timejson = palm.time_extract(text)
            if data["time"]=="" or data["time"]==None:
                speaker.speak("something went wrong")
                continue
            else:
                message=input("message")

                print(timejson)
        else:

            # speaker.speak(texts.pleasewaitlist[int(random.randint(0,(texts.pleasewaitlist.__len__())-1))])
            speaker.speak(palm.funny_reply("please wait the information is loading"))
            try:
                text=palm.get_bard_message(text)
            except Exception as ex:
                speaker.speak("error ocuured try again later")
                print(ex)
                text=""
            print(str(text))
            speaker.speak(text=text)

    elif "stop playback" in text:
        pass