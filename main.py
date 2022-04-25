import transmitter
import canal
import random
import decoder
import copy
import numpy as np

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
#print("POTROJONE:")
#[print(x, end='') for x in codedData]
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

trojki_in = np.array_split([item for sublist in packets for item in sublist], len(inputData))
trojki_out = np.array_split([item for sublist in packetsFalse for item in sublist], len(outputData))
print("trojki przed przejsciem przez kanal:")
print(*trojki_in) 
print()
print("trojki po przejsciu przez kanal:")
print(*trojki_out)
print()
roznice = []
duze_bledy = []
male_bledy = []
for pair in list(zip(trojki_in, trojki_out)):
    roznica = np.sum(pair[0] != pair[1])
    roznice.append(roznica)
counter = 0
for diff in roznice:
    if diff >= 2:
        duze_bledy.append(counter)
    elif diff >= 1:
        male_bledy.append(counter)
    counter += 1
print(f"ilosc roznych bitow pomiedzy trojkami: {roznice}")
print(f"indeksy duzyc bledow: {duze_bledy}")
print(f"indeksy malych bledow: {male_bledy}")

print()
print("Dane wyjsciowe: ")
[print(x,'',end='') for x in outputData]
print()

print("Bledy ktorych nie udalo sie naprawic: " + str(check()))
