import numpy as np

class Decoder():
    def decoding(self, data):
        l = []
        it = 0
        zeros = 0
        ones = 0
        for i in data:
            for j in i:
                it = it + 1
                if it == 3:
                    if zeros > ones:
                        #print("ZERO")
                        l.append(0)
                    else:
                        #print("JEDEN")
                        l.append(1)
                        
                    zeros = 0
                    ones = 0
                    it = 0

                if j == 0:
                    zeros = zeros + 1
                elif j == 1:
                    ones = ones + 1


        return l
        
    def unpack(self):
        return
