from naoqi import ALProxy
from audio import get_string


def related_actions(string):
    tts = ALProxy("ALTextToSpeech", "192.168.1.155", 9559)
    print 'Recognized: {}'.format(string)
    if 'stand' in '{}'.format(string):
        try:
            postureProxy = ALProxy("ALRobotPosture", "192.168.1.155", 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
        result = postureProxy.goToPosture("Stand", 1.0)
        if result:
            tts.say('It feels good to stand')

    elif 'sit' in '{}'.format(string):
        try:
            postureProxy = ALProxy("ALRobotPosture", "192.168.1.155", 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
        result = postureProxy.goToPosture("Sit", 1.0)
        if result:
            tts.say("Finally Sitting")

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
