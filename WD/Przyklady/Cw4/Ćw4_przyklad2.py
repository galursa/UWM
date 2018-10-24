import sys

print("Podaj kierunek studiów, rok i specjalność")

#odczyt danych ze standadrdowego wejścia
dane =sys.stdin.readline()

#Otwieramy plik
plik=open("dane.txt","w+")

#Zpaisujemy do pliku
plik.write(dane)

#zamykamy plik
plik.close()

#tworzymy liste
lista=[]
for x in range(1,6,1):
    lista += [x]

#otwieramy plik do dopisywania
plik=open("dane.txt","a+")

#zapisujemy
plik.writelines(str(lista))

#zamykamy
plik.close()
