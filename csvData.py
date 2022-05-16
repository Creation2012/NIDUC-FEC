import csv

pola = ['g','b']

def dataToFile(g, b):
    with open('data.csv', mode='a') as csvFile:
        writer = csv.DictWriter(csvFile, delimiter=';', fieldnames=pola)
        merg = [{'g':g, 'b':b}]
        for x in merg:
            writer.writerow(x)
