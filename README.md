# System FEC
**Kodowanie korekcyjne** lub **kodowanie korygujące** (FEC – _forward error correction_) – technika dodawania [nadmiarowości](https://pl.wikipedia.org/wiki/Redundancja "Redundancja") do [transmitowanych](https://pl.wikipedia.org/wiki/Transmisja "Transmisja") [cyfrowo](https://pl.wikipedia.org/wiki/Sygna%C5%82_cyfrowy "Sygnał cyfrowy") [informacji](https://pl.wikipedia.org/wiki/Informacja "Informacja").

# Symulator
Symulator napisany w Pythonie 3.10.4.
Realizuje generowanie losowych danych wejściowych, przetwarzanie ich przez kanał transmisyjny i następnie na podstawie niżej przedstawionych algorytmów, dokonywana jest naprawa przesyłanych pakietów.

**Stosowane algorytmy:**
- Potrajanie bitów
- Rozszerzony kod Hamminga

**Kanały transmisyjne:**
- AWGN Channel
- Binary Symmetric Channel
- Discrete Memoryless Channel

# Uruchamianie
Program uruchamiany z linii komend, z podanymi argumentami:
```
python main.py [algorytm] [bity] [kanal]
```
- algorytm - do wyboru (1 - potrajanie bitow, 2 - kod Hamminga)
- bity - generowana ilosc bitow do przetworzenia
- kanal - kanal transmisyjny (1 - AWGN, 2 - BSC, 3 - DMC)
