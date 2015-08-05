#!/usr/bin/env python
import time

from audio import get_string
import nao_parser
import sys
import env
import threading

if len(sys.argv) > 1:
    env.nao_ip = sys.argv[1]
else:
    print "Usage: python speech_recognition.py [robot_ip] [port]"
    sys.exit()
if len(sys.argv) > 2:
    env.nao_port = sys.argv[2]


def speech_recognition_loop():
    while True:
        try:
            string = get_string()
        except LookupError as e:
            print e
        else:
            nao_parser.parse(string)


def face_detection_loop():
    pass

sr_t = threading.Thread(None, speech_recognition_loop, "sr_t")
sr_t.start()
fd_t = threading.Thread(None, face_detection_loop, "fd_t")
fd_t.start()
