import transmitter
import canal
import random
import decoder
import copy

def generate(n):
    for i in range(0,n):
        inputData.append(random.randint(0,1))

def check():
    x = 0 # ilosc zmienionych bitow
    for i,j in zip(inputData,decodedPacket):
        if i != j:
            x = x + 1
    return x


t = transmitter.Transmitter()
c = canal.Canal()
d = decoder.Decoder()

inputData = [] # dane wejsciowe

print("Podaj ilosc bitow do wygenerowania")
n = int(input())
generate(n)
print()

print("Dane wejsciowe:")
[print(x,'',end='') for x in inputData]
print('\n')

inputPacket = t.makePacket(inputData)

print("Pakiety z danych wejsciowych: ")
[print(x) for x in inputPacket]
print()
codedData = t.tripleBit(inputData) # potrojone bity
packets = t.makePacket(codedData) # pakiety

print("Pakiety po potrojeniu bitow: ")
[print(x) for x in packets]

print()

print("Podaj procent zaklocen (0 - 1): ")
rnd = float(input())

packetsFalse = copy.deepcopy(packets)
c.signalDistortion(packetsFalse,rnd)
print()

print("Pakiety po przejsciu przez kanal: " )
[print(x) for x in packetsFalse]

decodedPacket = d.decoding(packetsFalse)

print()
print("Dane wyjsciowe: ")
[print(x,'',end='') for x in decodedPacket]

print('\n')
print("Znieksztalcony sygnal/porownanie: ")
print(check())
