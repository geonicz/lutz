#!/usr/local/bin/python 

import sys
marker = '::::::'

while 1:
    line = sys.stdin.readline()                 # read next line
    if not line:
        break                                   # exit on end-of-file
    elif line[:6] != marker:
        print line,                             # or copy real line
    else:
        sys.stdout = open(line[6:-1], 'w')      # or new output file
