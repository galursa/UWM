#biblioteka potrzebna do obsługi plików csv
import csv

#w nawiasie podajemy nazwę naszego pliku tutaj jest to data.csv
csvfile = open('data-text.csv','r')
#przekazujemy csvfile do funkcji reader w module csv
#efekt działania funkcji reader będzie znajdował się w zmiennej read
read = csv.DictReader(csvfile)

for row in read:
    print(row)
