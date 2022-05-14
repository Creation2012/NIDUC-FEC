import numpy

class Transmitter:
    # Error correction by triple bits
    def tripleBit(self, data):
        return numpy.repeat(data,3).tolist()

    def makePacket(self, data, bits):
        packetList = [data[x:x+bits] for x in range(0, len(data), bits)]
        return packetList

    # Error correction by hamming
    def hamMakePacket(self, data, parity):
        for i in parity:
            p = 0
            for j in range(i+1,len(data)):
                if j & i == i and j not in parity:
                    if data[j] == 1:
                        p = p + 1

            data[i] = p % 2 

        c = 0

        for i in range(1, len(data)):
            if data[i] == 1:
                c = c + 1

        data[0] = c % 2

        return data

    def hamParityBits(self, bits):
        l = list()
        l.append(0)
        n = 0
        while pow(2,n) < bits:
            l.append(pow(2,n))
            n = n + 1

        return l

