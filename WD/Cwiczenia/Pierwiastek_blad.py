import math

#Cwiczenie 2
#Zad 14
print("Liczę pierwiastek \n")
liczba=input("Podaj liczbę ")
liczba=int(liczba)

try:
    pierwiastek=math.sqrt(liczba)
    print(str(pierwiastek))
except Exception:
    print("Podano nie właściwą liczbę")
    

