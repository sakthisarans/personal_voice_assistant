from AppOpener import open as o

from a_vcontroll import listen, speak


def open_application(appname):
    try:
        print(o(appname,match_closest=True,throw_error=True))
        speak.speak("enjoy your raide")
    except:
        speak.speak("Application not found")