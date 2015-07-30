#!/usr/bin/env python

from naoqi import ALProxy
import actions
import env

understandableWords = ["sit", "stand", "say"]
helloWords = ["hello", "hi", "hey"]
priorityWords = ["now"]
actionsArray = []


def cut_sentence(sentence):
    words = sentence.split(" ")
    for word in words:
        if word in priorityWords:
            # get the last item and put it first
            actionsArray.insert(0, actionsArray.pop())
        if word in understandableWords or word in helloWords:
            actionsArray.append(word)
    return actionsArray


def send_next():
    if actionsArray:
        # TODO send the action.
        actions.do_action(actionsArray.pop(0))


def parse(string):
    print 'Recognized: {}'.format(string)
    tts = ALProxy("ALTextToSpeech", env.nao_ip, env.nao_port)
    cut_sentence(string)
    actions.do_action(send_next)
    tts.say("What should I do now ?")
