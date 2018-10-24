#pobieramy od użytkownika liczbę i sprawdzamy czy jest podzielna przez 3
try:
    ile=input("ile chcesz liczb?")
    ile=int(ile)
    for i in range(ile):
        liczba=input("Proszę podać liczbę ")
        liczba=int(liczba)
        if (liczba%3)==0:
            print("Liczba jest podzielna przez 3")
        else:
            print("Liczba nie jest podzielna przez 3")
            
except ValueError:
    print("Podano nieprawidłową liczbę")
