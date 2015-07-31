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
    rowing = False
    postureProxy = None
    try:
        postureProxy = ALProxy("ALRobotPosture", env.nao_ip, env.nao_port)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    if 'stand' in '{}'.format(string) and postureProxy is not None:
        postureProxy.goToPosture("Stand", 1.0)

    elif 'sit' in '{}'.format(string) and postureProxy is not None:
        postureProxy.goToPosture("Sit", 1.0)

    elif 'moonwalk' in '{}'.format(string):
        if postureProxy.getPosture() != "Stand":
            postureProxy.goToPosture("Stand", 1.0)

        walk_to_position(-1.0, 0.0, 0.0, 1)

    elif 'walk' in '{}'.format(string):
        if postureProxy.getPosture() != "Stand":
            postureProxy.goToPosture("Stand", 1.0)
        walk_to_position(0.2, 0.3)
    elif 'row' in '{}'.format(string):
        if not env.global_rowing:
            env.global_rowing = True
            rowing = True
        else:
            tts = ALProxy("ALTextToSpeech", env.nao_ip, env.nao_port)
            volume = tts.getVolume()
            tts.setVolume(1)
            tts.say("Fight the Power")
            tts.setVolume(volume)

    if not rowing:
        env.global_rowing = False


    # else:
    #     from pygoogle import pygoogle
    #     g = pygoogle('{}'.format(string))
    #     g.pages = 1
    #     print '*Found %s results*' % (g.get_result_count())
    #     import pdb; pdb.set_trace()
    #     g.get_urls()
