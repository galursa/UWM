#Użytkownik podaje liczbę
#Przeglądamy listę liczb i jeśli znajdziemy tę podaną przez użytkownika
#wyświetlamy komunikat i kończymy działanie pętli

lista = [1, 5, 3, 2, 6, 7, 8, 9, 10]
print("Podaj liczbę a sprawdzę czy jest na liście")
liczba=input()
licznik=0
while licznik<10: 
    #Jeśli znajdziemy liczbę przerywamy
    if int(liczba) == lista[licznik]:
        print("Twoja liczba: "+liczba+"znaleziona na pozycji: "+str(licznik))
        break
    else:
       licznik+=1
