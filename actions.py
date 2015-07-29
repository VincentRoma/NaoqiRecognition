#!/usr/bin/env python

from naoqi import ALProxy
from audio import get_string
import sys

if len(sys.argv) > 1:
    nao_ip = sys.argv[1]
else:
    print "Usage: python actions.py [robot_ip] [port]"
    sys.exit()
if len(sys.argv) > 2:
    nao_port = sys.argv[2]
else:
    nao_port = 9559


def walk_to_position(nao_ip, port, x, y, teta=0.0, freq=0):
    try:
        motionProxy = ALProxy("ALMotion", nao_ip, port)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    X = x
    Y = y
    Theta = teta
    Frequency = freq  # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


def related_actions(string):
    tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
    print 'Recognized: {}'.format(string)
    if 'stand' in '{}'.format(string):
        try:
            postureProxy = ALProxy("ALRobotPosture", nao_ip, nao_port)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
        result = postureProxy.goToPosture("Stand", 1.0)
        if result:
            tts.say('It feels good to stand')

    elif 'sit' in '{}'.format(string):
        try:
            postureProxy = ALProxy("ALRobotPosture", nao_ip, nao_port)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
        result = postureProxy.goToPosture("Sit", 1.0)
        if result:
            tts.say("Finally Sitting")

    elif 'walk' in '{}'.format(string):
        walk_to_position(nao_ip, nao_port, 0.2, 0.3)

    # else:
    #     from pygoogle import pygoogle
    #     g = pygoogle('{}'.format(string))
    #     g.pages = 1
    #     print '*Found %s results*' % (g.get_result_count())
    #     import pdb; pdb.set_trace()
    #     g.get_urls()
    tts.say("What should I do now ?")

while(True):
    related_actions(get_string())
