import os
class HelloWorld(object):
    def __init__(self,it):
        self.it = it
    def printf(self):
        print("Hello,%s!" %(self.it))

class HelloAgain(HelloWorld):
    def __init__(self,it):
        self.it = it
def Hello(it):
    print("Hello,%s" %(it))
class Hello(HelloWorld):
    def __init__(self,it):
        self.it = it
    def Hello(self):
        Hello(self.it)

Jack = HelloWorld("Jack")
Jack.printf()
print("%s" %(None))