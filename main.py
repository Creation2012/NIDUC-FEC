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
    for i,j in zip(inputData,outputData):
        if i != j:
            x = x + 1
    return x

def check2():
    x = 0
    for i, j in zip(packets, packetsFalse):
        return

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

outputData = d.decoding(packetsFalse)

print()
print("Dane wyjsciowe: ")
[print(x,'',end='') for x in outputData]

print('\n')
print("Bledy ktorych nie udalo sie naprawic: ")
print(check())
