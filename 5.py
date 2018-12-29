#!/usr/bin/env python3

class test(object):
    def __init__(self):
        self.s = ""

    def getstring(self):
        self.s = input()

    def printstring(self):
        print(self.s.upper())


obj = test()
obj.getstring()
obj.printstring()
