#otwarcie pliku do odczytu

plik = open("Ćw1_przyklad1.py","r")

#odczyt 10 znaków z pliku
znaki = plik.read(10)

#odczyt jednej lini z pliku
linia = plik.readline()

#odczyt wierszy z pliku
wiersze = plik.readlines()

#zamkniecie pliku
plik.close()

#drukujemy 10 znakow
print(znaki)
print("\n")

#drukujemy linię
print(linia)
print("\n")

#drukujemy cały plik
print(wiersze)
print("\n")




