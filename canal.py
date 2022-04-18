import random

class Canal:
    def signalDistortion(self, p, rnd):
        for i in p:
            for j in range(0,len(i)):
                if random.random() < rnd:
                    if i[j] == 0:
                        i[j] = 1
                    else:
                        i[j] = 0
