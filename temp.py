class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        import sys, os
        import pdb; pdb.set_trace()
        
        self.logger.debug("Loading speech_recognition module")
        framemanager = ALProxy("ALFrameManager")
        folderName = os.path.join(framemanager.getBehaviorPath(self.behaviorId),"~/.virtualenvs/proj/lib/python2.7/site-packages")
        self.logger.debug("Loading {}".format(folderName))
        if folderName not in sys.path:
            sys.path.append(folderName)
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.logger.debug("Starting Recording")
            audio = r.listen(source)

        try:
            self.logger.debug("You said " + r.recognize(audio))
        except LookupError:
            self.logger.debug("Could not understand audio")


    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
