import transmitter
import canal
import random
import decoder
import csvData
import copy
import numpy as np
import komm as ko
import sys
from functools import reduce

# argument 1 - ilosc prob
# argument 2 - 1) potrajanie bitow, 2) hamming
# argument 3 - ilosc bitow (liczba calkowita n)
# argument 4 - kanal transmisyjny (tylko dla potrajania bitow)

def generate(n):
    for i in range(0,n):
        inputData.append(random.randint(0,1))

def check():
    x = 0 # ilosc zmienionych bitow
    for i,j in zip(inputData,outputData):
        if i != j:
            x = x + 1
    return x

def main(x = int(sys.argv[2]), n = int(sys.argv[3]), tChoose = int(sys.argv[4])):

    #x = int(sys.argv[1])

    if x == 1:
        #n = int(sys.argv[2]) # ilosc bitow do wygenerowania

        generate(n)

        codedData = t.tripleBit(inputData) # potrojone bity
        packets = t.makePacket(codedData, 255) # pakiety

        #print("1) Kanal AWGN")
        awg = ko.AWGNChannel(snr=100.0, signal_power=1.0)
        #print("2) Kanal Binary Symmetric Channel")
        bsc = ko.BinarySymmetricChannel(0.5)
        #print("3) Kanal Discrete Memoryless Channel")
        dmc = ko.DiscreteMemorylessChannel([[0.5, 0.5], [0.5, 0.5]])
        
        #tChoose = int(sys.argv[3]) 

        packetsFalse = copy.deepcopy(packets)
        y = list()
        y2 = list()
        if tChoose == 1:
            for i in packetsFalse:
                y.append(awg(i))

            [y2.append(list(map(int,i))) for i in y]

            packetsFalse = y2
        elif tChoose == 2:
            for i in packetsFalse:
                y.append(bsc(i))

            packetsFalse = y
        
        elif tChoose == 3:
            for i in packetsFalse:
                y.append(dmc(i))

            packetsFalse = y

        #print("Pakiety po przejsciu przez kanal: " )
        #[print(x) for x in packetsFalse]

        outputData = d.decoding(packetsFalse)

        trojki_in = np.array_split([item for sublist in packets for item in sublist], len(inputData))
        trojki_out = np.array_split([item for sublist in packetsFalse for item in sublist], len(outputData))
        #print("trojki przed przejsciem przez kanal:")
        #print(*trojki_in) 
        #print()
        #print("trojki po przejsciu przez kanal:")
        #print(*trojki_out)
        #print()
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
        #print(f"ilosc roznych bitow pomiedzy trojkami: {roznice}")
        #print(f"indeksy duzyc bledow: {duze_bledy}")
        #print(f"indeksy malych bledow: {male_bledy}")

        csvData.dataToFile(n, len(duze_bledy))
        #print()
        #print("Dane wyjsciowe: ")
        #[print(x,'',end='') for x in outputData]
        #print()

        #print("Bledy ktorych nie udalo sie naprawic: " + str(check()))

    elif x == 2:
        #n = int(sys.agrv[1]) 

        dim = lambda m: 2**m - m - 1
        red = 2
        while n != dim(red) :
            if n < dim(red):
                print("Podaj inna ilosc bitow")
                n = int(input())
                red = 1
            red = red + 1

        code = ko.HammingCode(red, extended=True)
        generate(n)

        #print("Dane wejsciowe (bez obliczonych parzystosci):")
        #[print(x,'',end='') for x in inputData]
        #print('\n')

        #print("Wygenerowany ciag bitow")
        #for i in range(0,len(inputData)):
        #    print(inputData[i],'',end='')

        #codedData = t.hamMakePacket(inputData, parityBits) 

        #print("Spakowany ciag bitow (z wyliczonymi bitami parzystosci)")
        #for i in range(len(codedData)):
        #    print('%3d, ' %codedData[i], end='')

        #    if(i+1) % len(inputData)**(1/2) == 0:
        #        print()

        #print("Zakodowany pakiet")
        codedData = code.encode(inputData)
        #print(codedData)
        #print()
        bsc = ko.BinarySymmetricChannel(0.5)

        #print("Pakiet po przejsciu przez kanal (1 - error)")
        y = bsc(codedData)

        #print(y)
        #print("Wykrycie bledu")
        detectError = d.hamDetectError(y)
        #print(detectError)

        y = code.decode(y)

        #print("Po dekodowaniu")
        #print(y)

        #d.hamRepair(y, detectError)

        #print("Naprawiony sygnal")

        #for i in range(len(y)):
        #    if i == detectError:
        #        print('(%1d),' %y[i], end='')
        #    else:
        #        print('%3d,' %y[i], end='')
        #    if(i+1) % len(inputData)**(1/2) == 0:
        #        print()

for i in range(0,int(sys.argv[1])):
    t = transmitter.Transmitter()
    c = canal.Canal()
    d = decoder.Decoder()

    inputData = []
    main()
