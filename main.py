import transmitter
import canal
import random

def generate(n):
    for i in range(0,n):
        rawData.append(random.randint(0,1))

t = transmitter.Transmitter()
c = canal.Canal()

rawData = []
generate(40)

rawData = t.tripleBit(rawData) # po potrojeniu
rawData = t.makePacket(rawData) # po zrobieniu pakietow

print("Pakiety: ")
[print(x) for x in t.packetList]

print()

c.signalDistortion(t.packetList)

print("Pakiety po przejsciu przez kanal" )
[print(x) for x in t.packetList]
