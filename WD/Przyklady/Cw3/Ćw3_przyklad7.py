#symbol * oznacza dowolną ilość argumentów przechowywanych w krotce

def ciag(* liczby):
    #jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0.0
    else:
        suma = 0.0

        #sumujemy elementy ciągu
        for i in liczby:
            suma += i
        #zwracamy wartość sumy
        return suma
#wywołanie gdy brak argumentów
print(ciag())
#podajemy argumenty
print(ciag(1,2,3,4,5,6,7,8))

