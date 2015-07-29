#!/usr/bin/env python

def get_string():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    if audio.data:
        return r.recognize(audio)
    else:
        return 0
