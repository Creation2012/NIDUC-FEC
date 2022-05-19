import csv

pola = ['nr','send','errors']

def dataToFile(g, b):
    with open('data.csv',mode='r') as csvFile:
        reader = csv.reader(csvFile)
        row = []
        for i in reader:
            row.append(i)

        if len(row) < 2:
            nr = 1
        else:
            nr = row[len(row)-2][0].split(';')[0]
            nr = int(nr)
            nr = nr + 1 

    with open('data.csv', mode='a') as csvFile:
        writer = csv.DictWriter(csvFile, delimiter=';', fieldnames=pola)
        merg = [{'nr':nr, 'send':g, 'errors':b}]
        for x in merg:
            writer.writerow(x)
