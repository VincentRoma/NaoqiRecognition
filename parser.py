#!/usr/bin/env python

from naoqi import ALProxy
import actions
import env


def parse(string):
    print 'Recognized: {}'.format(string)
    tts = ALProxy("ALTextToSpeech", env.nao_ip, env.nao_port)
    actions.do_action(string)
    tts.say("What should I do now ?")
