import numpy

class Transmitter:
    def tripleBit(self, data):
        return numpy.repeat(data,3).tolist()

    def makePacket(self, data):
        packetList = [data[x:x+30] for x in range(0, len(data), 30)]
        return packetList
