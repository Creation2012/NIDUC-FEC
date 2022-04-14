import random

class Canal:
    def signalDistortion(self, package):
        for i in package:
            for j in range(0,len(i)):
                 i[j]= random.randint(0,1)
