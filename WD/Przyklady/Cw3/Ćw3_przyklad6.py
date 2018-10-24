#Definiujemy funkcje z wartościami domyślnymi
import math

def dlugosc_odcinka(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#wywołujemy dla wartości domyślnych
print(dlugosc_odcinka())

#wywolujemy dla własnych podanych wartości
#są to argumenty pozycjne czyli ważna jest kolejnosć podania wartości
print(dlugosc_odcinka(1, 2, 3, 4))

#Wywolujemy funkcje podając mieszane wartości
#Dwie pierwsze są interpretowane jako x1 i y1 jak podano w definicji funkcji
print(dlugosc_odcinka(2, 2, y2 = 2, x2 = 1))

#wywołujemy funkcje pdoając wartości nie w kolejności
print(dlugosc_odcinka(y2 = 5, x1 = 2, y1 = 2, x2 = 6))

#wywołujemy funkcję podając tylko dwa argumenty a reszta domyślne
print(dlugosc_odcinka(x2 = 5, y2 = 5))
