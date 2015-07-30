#!/usr/bin/env python

import actions

understandableWords = ["sit", "stand", "walk", "moonwalk", "row"]
helloWords = ["hello", "hi", "hey"]
priorityWords = ["now"]
actionsArray = []


def cut_sentence(sentence):
    words = sentence.split(" ")
    print(words)
    for word in words:
        if word in priorityWords:
            # get the last item and put it first
            actionsArray.insert(0, actionsArray.pop())
        if word in understandableWords or word in helloWords:
            actionsArray.append(word)
    return actionsArray


def send_next():
    while actionsArray:
        action = actionsArray.pop(0)
        print action
        actions.do_action(action)


def parse(string):
    print 'Recognized: {}'.format(string)
    cut_sentence(string)
    send_next()
    return None
