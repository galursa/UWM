#Pobieramy od użytkownika liczbę
#Chcemy sprawdzić czy jest dodatnia czy ujemna

l=input("Podaj jakąś liczbę")

#l jest typu string musimy ją rzutować na całkowitą

l=int(l)

if l > 0:
    print("Podano liczbę dodatnią")
elif l < 0:
    print("Podano liczbę ujemną")
else:
    print("Podano liczbe równą zero")
