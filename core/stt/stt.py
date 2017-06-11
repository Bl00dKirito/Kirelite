import os
import time
import speech_recognition as sr

import telepot

import profile
from tts import tts


def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        tts("Prova a dire qualcosa!")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(
            audio).lower().replace("'", "")
        print("Penso tu abbia detto '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Non ho capito")
    except sr.RequestError as e:
        tts(
            "Non sono riuscita a contattare Google" +
            "Speech Recognition service; {0}".format(e))
    else:
        return speech_text

    if profile.data['keyboard'] == 'on':

        keyboard_text = raw_input('Write something: ')
        return keyboard_text
