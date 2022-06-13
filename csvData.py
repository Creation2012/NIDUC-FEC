import csv
import pandas as pd

pola = ['nr','send','errors']

def dataToFile(nr, send, errors):
    with open('data.csv', mode='a',newline='') as csvFile:
        writer = csv.DictWriter(csvFile, delimiter=';', fieldnames=pola)
        merg = [{'nr':nr, 'send':send, 'errors':errors}]
        if nr == 1:
            writer.writeheader()

        for x in merg:
            writer.writerow(x)

def clearFile():
    open('data.csv', 'w').close()
