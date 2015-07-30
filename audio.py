#!/usr/bin/env python


def get_string():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    if audio.data:
        response = r.recognize(audio)
        
        return response
    else:
        return 0
