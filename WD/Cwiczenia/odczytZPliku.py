plik = open("dzielenie.py","r")
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

#odczyt z polskimi literami
with open('dzielenie.py', encoding='utf-8') as plik:
    for linia in plik:
        print(repr(linia))

#odczyt z polskimi literami wersja skrócona
plik = open("dzielenie.py","r",encoding='utf-8')
wiersze = plik.readlines()
print(wiersze)
