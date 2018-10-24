#pobieramy od użytkownika liczbę
#losujemy liczby tyle razy ile użytkownik podał
#każdą liczbe dodajemy na listę

import random

ileLosuj=input("Proszę podać ile liczb ma być wylosowanych")
ileLosuj=int(ileLosuj)
lista=[]
for i in range(ileLosuj):
    z=random.random()
    #print(str(z)+" ")
    lista.append(z)
print(lista)
