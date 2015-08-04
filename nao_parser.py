#!/usr/bin/env python

from naoqi import ALProxy
import actions
import env
import math
import re
import random

understandableWords = ["sit", "stand", "walk", "moonwalk", "row", "start", "stop", "face"]
understandableSentences = [
    "how are you",
    "thank you",
]
helloWords = ["hello", "hi", "hey"]
priorityWords = ["now"]
startWords = ["start", "begin"]
stopWords = ["stop"]
pleaseWords = ["please"]
pleasedAnswers = [
    "Sure !",
    "Right away !",
    "Yes.",
    "Ok, I'll do it."
]
actionsArray = []


def spot_sentence(string):
    for try_sentence in understandableSentences:
        try_len = len(try_sentence.split(" "))
        string_len = len(string.split(" "))
        if string_len > int(math.ceil(try_len * 1.4)):
            continue
        if re.match("^.*"+try_sentence.replace(" ", ".*")+".*$", string, re.DOTALL | re.IGNORECASE):
            print "^.*"+string.replace(" ", ".*")+".*$"
            actionsArray.append(try_sentence)
            return try_sentence

    return False


def cut_sentence(sentence):
    defined_sentence = spot_sentence(sentence)
    if defined_sentence:
        print defined_sentence
        return

    words = sentence.split(" ")
    print(words)
    for word in words:
        if word in startWords:
            env.nao_listening = True
        elif word in stopWords:
            env.nao_listening = False
        elif word in pleaseWords:
            actions.add_positive()
            env.nice_demand = True

        if not env.nao_listening:
            continue
        if word in priorityWords:
            # get the last item and put it first
            actionsArray.insert(0, actionsArray.pop())
        elif word in understandableWords or word in helloWords:
            actionsArray.append(word)
    return actionsArray


def send_next():
    if not actionsArray:
        return
    if env.nice_demand:
        tts = ALProxy("ALTextToSpeech", env.nao_ip, env.nao_port)
        tts.say(random.choice(pleasedAnswers))
    while actionsArray:
        action = actionsArray.pop(0)
        print action
        actions.do_action(action)
    env.nice_demand = False


def parse(string):
    print 'Recognized: {}'.format(string)
    cut_sentence(string)
    send_next()
    return None
