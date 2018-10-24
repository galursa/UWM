#skrypt wyświetla losowe liczby całkowite aż napotka 5

import random #biblioteka z funkcjami do losowania

random.seed() #inicjowanie generatora

z=random.randint(1,15) #losowanie pierwszej liczby

while(z!=5):
    print(str(z))
    z=random.randint(1,15)
else:
    print("Znalazłem 5 koniec działania")
