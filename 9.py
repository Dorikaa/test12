#!/usr/bin/env python3

#
#import sys
#
#a = sys.stdin.readline()
#b = sys.stdin.readline()
#
#a = a.upper()
#b = b.upper()
#
#
#print(a)
#print(b)
#


#for more than 2 lines

import sys

lines = []
while True:
    s = input():
    if s:
        lines.append(s.upper())
    else:
        break

for seq in lines:
    print(seq)

