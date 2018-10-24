#Uzytkownik podaje liczby do dzielenia
#Chcemy wyłapać moment dzielenia przez zero
print("Proszę podać pierwszą liczbę")
licz1 = input()
print("Proszę podać drugą liczbę")
licz2 = input()
try:
    wynik = int(licz1) / int(licz2)
    print("Wynik= "+str(wynik))
except ZeroDivisionError: #nazwa błędu dzielenia przez zero
    print("Tylko Chuck Norris może dzielić przez zero!")
    
