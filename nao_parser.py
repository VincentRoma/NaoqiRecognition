#!/usr/bin/env python

from naoqi import ALProxy
import actions
import env
import math
import re
import random
import knock_jokes

understandableWords = ["sit", "stand", "walk", "moonwalk", "row", "face", "record", "recall", "joke", "yes", "no", "there", "who"]
understandableSentences = [
    "how are you",
    "thank you",
    "knock knock",
]
helloWords = ["hello", "hi", "hey"]
priorityWords = ["now"]
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
        if word in pleaseWords:
            actions.add_positive()
            env.nice_demand = True

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
    if env.knocking == 1:
        knock_jokes.current_knock = string
        print knock_jokes.current_knock
        actionsArray.append("knocked")
    if env.knocking == 2:
        knock_jokes.add_knock_joke(
            knock_jokes.current_knock,
            string,
        )
        knock_jokes.current_knock = ""
        actionsArray.append("nao_laugh")
        print knock_jokes.jokes
    else:
        cut_sentence(string)
    send_next()
    return None
