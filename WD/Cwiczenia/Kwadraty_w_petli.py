#2 ćwiczenia
#zadanie 7

ile=input("Podaj ile chcesz wczytać liczb: ")
ile=int(ile)

for i in range(ile):
    liczba=input("Podaj liczbę numer "+str(i)+": ")
    liczba=int(liczba)
    print(str(liczba**2))
    
