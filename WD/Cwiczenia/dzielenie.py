import sys
try:
    print("Dzięlę liczby przez siebie")
    print("Proszę podać pierwszą liczbę: ")
    licz1=sys.stdin.readline()
    print("Proszę podać drugą liczbę: ")
    licz2=sys.stdin.readline()
    licz1=float(licz1)
    licz2=float(licz2)
    wynik=licz1/licz2
    print(str(wynik))
except ZeroDivisionError:
    print("Wystąpiło dzielenie przez zero")
except ValueError:    
    print("podane wartości to nie liczby")
