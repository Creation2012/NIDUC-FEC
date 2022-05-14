import numpy as np
from functools import reduce

class Decoder():
    def decoding(self, packet):
        l = []
        it = 0
        zeros = 0
        ones = 0
        for i in packet:
            for j in i:
                if j == 0:
                    zeros = zeros + 1
                elif j == 1:
                    ones = ones + 1

                it = it + 1

                if it == 3:
                    if zeros > ones:
                        l.append(0)
                    elif zeros < ones:
                        l.append(1)
                        
                    zeros = 0
                    ones = 0
                    it = 0
                if it == 3:
                    if zeros > ones:
                        l.append(0)
                    elif zeros < ones:
                        l.append(1)
                        
                    zeros = 0
                    ones = 0
                    it = 0
        return l
        
    def unpack(self):
        return

    # Hamming Error Correction

    def hamDetectError(self, data):
        return reduce(lambda x, y: x^y, [i for i, bit in enumerate(data) if bit and i != 0])

    def hamRepair(self, data, x):
        data[x] ^= 1
