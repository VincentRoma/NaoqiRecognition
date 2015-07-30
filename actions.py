#!/usr/bin/env python

from naoqi import ALProxy
import env


def walk_to_position(x, y, theta=0.0, freq=0.0):
    try:
        motion_proxy = ALProxy("ALMotion", env.nao_ip, env.nao_port)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
    else:
        motion_proxy.moveToward(x, y, theta, [["Frequency", freq]])


def do_action(string):
    tts = ALProxy("ALTextToSpeech", env.nao_ip, env.nao_port)
    postureProxy = None
    try:
        postureProxy = ALProxy("ALRobotPosture", env.nao_ip, env.nao_port)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    if 'stand' in '{}'.format(string) and postureProxy is not None:
        result = postureProxy.goToPosture("Stand", 1.0)
        if result:
            tts.say('It feels good to stand')

    elif 'sit' in '{}'.format(string) and postureProxy is not None:
        result = postureProxy.goToPosture("Sit", 1.0)
        if result:
            tts.say("Finally Sitting")

    elif 'walk' in '{}'.format(string):
        walk_to_position(env.nao_ip, env.nao_port, 0.2, 0.3)

    # else:
    #     from pygoogle import pygoogle
    #     g = pygoogle('{}'.format(string))
    #     g.pages = 1
    #     print '*Found %s results*' % (g.get_result_count())
    #     import pdb; pdb.set_trace()
    #     g.get_urls()
