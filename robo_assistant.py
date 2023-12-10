import datetime
import webbrowser

import pyjokes
import pyttsx3 as pyt
import speech_recognition as sr


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("recognizing..")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not understanding .. ")

def speechtx(x):
    engine = pyt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()

speechtx("Welcome to Uttam's assistant")

if __name__ == '__main__':
    # if sptext().lower()=="hello robo":
    MYDATA =sptext().lower()
       
    if "your name" in MYDATA:
        name = "my name is robo assistant"
        speechtx(name)

    elif "old are you" in MYDATA:
        age = "I have no age, I was made a year ago"
        speechtx(age)

    elif "time now" in MYDATA:
        time = datetime.datetime.now().strftime("%I%M%p")

    elif "youtube" in MYDATA:
        webbrowser.open("https://www.youtube.com/")

    else:
        print("i am not understand")
        

else:
    print("Thank you")

