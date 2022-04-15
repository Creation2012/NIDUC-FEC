import transmitter
import canal
import random
import decoder

def generate(n):
    for i in range(0,n):
        rawData.append(random.randint(0,1))

t = transmitter.Transmitter()
c = canal.Canal()
d = decoder.Decoder()

rawData = []
generate(42)

print("Dane wejsciowe:")
[print(x,'',end='') for x in rawData]
print("Dlugosc: ", len(rawData))
print()

codedData = t.tripleBit(rawData) # po potrojeniu
packets = t.makePacket(codedData) # po zrobieniu pakietow

print("Pakiety: ")
[print(x) for x in packets]

print()

c.signalDistortion(packets)

print("Pakiety po przejsciu przez kanal" )
[print(x) for x in packets]

decodedPacket = d.decoding(packets)

print()
print("Dane wyjsciowe: ")
[print(x,'',end='') for x in decodedPacket]
print("Dlugosc: ", len(decodedPacket))
