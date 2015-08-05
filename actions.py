#!/usr/bin/env python

from naoqi import ALProxy
import env
import time
import knock_jokes


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
    tts = ALProxy("ALTextToSpeech", env.nao_ip, env.nao_port)
    try:
        postureProxy = ALProxy("ALRobotPosture", env.nao_ip, env.nao_port)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    if env.joking_knock and not 'there' in '{}'.format(string):
        tts.say("You were supposed to say : who's there !")
    elif 'there' in '{}'.format(string):
        tts.say(str(knock_jokes.jokes[0]['first']))
        env.joking_knock_second = True
        env.joking_knock = False
    elif 'who' in '{}'.format(string) and env.joking_knock_second:
        tts.say(str(knock_jokes.jokes[0]['second']))
        env.joking = False
        env.joking_knock = False
        env.joking_knock_second = False
        tts.say("Hah hah hah ! Hah hah hah ! Hah hah ! Hehe ! Weehee !")
        if postureProxy.getPosture() != "Stand":
            postureProxy.goToPosture("Stand", 1.0)

        walk_to_position(-1.0, 0.0, 0.0, 1)
    elif 'how are you' in '{}'.format(string):
        tts.say("I'm fine, how are you ?")
    elif 'thank you' in '{}'.format(string):
        tts.say("You're welcome !")
        add_positive()
    elif 'stand' in '{}'.format(string) and postureProxy is not None:
        postureProxy.goToPosture("Stand", 1.0)

    elif 'sit' in '{}'.format(string) and postureProxy is not None:
        postureProxy.goToPosture("Sit", 1.0)

    elif 'joke' in '{}'.format(string):
        tts.say("Yay! I love jokes !")

    elif 'knock knock' in '{}'.format(string):
        tts.say("Who's there ?")
        env.knocking = 1

    elif 'knocked' in '{}'.format(string):
        if env.knocking == 1:
            tts.say(str(knock_jokes.current_knock + " who ?"))
            env.knocking = 2
    elif 'nao_laugh' in '{}'.format(string):
        tts.say("Hah hah hah hah hah !")
        env.knocking = 0
        knock_jokes.joke_for_you = True

    elif 'face' in '{}'.format(string):
        tts = ALProxy("ALFaceDetection", env.nao_ip, env.nao_port)
        tts.enableTracking(True)
        tts.learnFace("damien")
        ALProxy("ALPhotoCaptureProxy", env.nao_ip, env.nao_port).takePicture()
    elif 'record' in '{}'.format(string) or 'recall' in '{}'.format(string):
        audioProxy = ALProxy("ALAudioRecorder", env.nao_ip, env.nao_port)
        audioProxy.startMicrophonesRecording("/home/nao/test.wav", "wav", 16000, [1, 1, 1, 1])
        time.sleep(15)
        audioProxy.stopMicrophonesRecording()

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
            volume = tts.getVolume()
            tts.setVolume(1)
            tts.say("Fight the Power")
            tts.setVolume(volume)
    elif 'hello' in '{}'.format(string):
        alas = ALProxy('ALAnimatedSpeech', env.nao_ip, env.nao_port)
        alas.say("^startTag(hello) Hello !^stopTag(hello)")
        if knock_jokes.joke_for_you:
            tts.say("Hey, do you want to hear a joke ?")
        env.joking = True
    elif 'no' in '{}'.format(string) and env.joking:
        tts.say("You're missing on something !")
        env.joking = False
    elif 'yes' in '{}'.format(string) and env.joking:
        tts.say("Knock knock !")
        env.joking_knock = True

    if not rowing:
        env.global_rowing = False

    # else:
    #     from pygoogle import pygoogle
    #     g = pygoogle('{}'.format(string))
    #     g.pages = 1
    #     print '*Found %s results*' % (g.get_result_count())
    #     import pdb; pdb.set_trace()
    #     g.get_urls()


def add_positive():
    env.nao_state_positive += 0.01
    if env.nao_state_positive > 1:
        env.nao_state_positive = 1
    print env.nao_state_positive
