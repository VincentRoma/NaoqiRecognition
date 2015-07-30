#!/usr/bin/env python

from audio import get_string
import nao_parser
import sys
import env

if len(sys.argv) > 1:
    env.nao_ip = sys.argv[1]
else:
    print "Usage: python speech_recognition.py [robot_ip] [port]"
    sys.exit()
if len(sys.argv) > 2:
    env.nao_port = sys.argv[2]

# Main loop
while True:
    try:
        string = get_string()
    except LookupError as e:
        print e
    else:
        nao_parser.parse(string)
