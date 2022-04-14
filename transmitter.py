import numpy

class Transmitter:
    def __init__(self):
        self.packet = []
        self.packetList = []

    def tripleBit(self, data):
        return numpy.repeat(data,3).tolist()

    def makePacket(self, data):
        self.packetList = [data[x:x+30] for x in range(0, len(data), 30)]
