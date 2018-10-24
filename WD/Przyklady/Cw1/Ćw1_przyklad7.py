#Tworzymy przykładową listę z danymi różnych typów
lista=["Ala", 3.14, 2, 1e30, [1,2,3]]
print('Zadeklarowana lista:\n',lista)
#dodamy element na koniec
lista.append("ostatni")
print('Lista po zmianach:\n',lista)
#dodamy element na drugim miejscu
lista.insert(1,"kot")
print('Lista po zmianach:\n',lista)
#usuwamy ostatni element
lista.pop()
print('Lista po zmianach:\n',lista)
#usuwamy element na wybranej pozycji
lista.pop(1)
print('Lista po zmianach:\n',lista)
#usuwamy element znając jego wartość
lista.remove(3.14)
print('Lista po zmianach:\n',lista)
#usuwamy element znając jego indeks
del lista[2]
print('Lista po zmianach:\n',lista)
#dodawanie sekwencji elementów do listy
lista.extend((1,2,3,4,5))
print('Lista po zmianach:\n',lista)
#zmiana wartości wybranego elementu
lista[0]="Ela"
print('Lista po zmianach:\n',lista)
#usuwanie fragmentu listy
del lista[3:5]
print('Lista po zmianach:\n',lista)
#przypisanie nowych wartości do podanego wycinka
lista[3:6]=[1,2,3]
#Odwracanie kolejności
lista.reverse()
print('Lista po zmianach:\n',lista)
nowa=[5,3,2,6,1,3,2]
#Sortowanie
print('Nowa lista:\n',nowa)
nowa.sort()
print('Nowa lista po zmianach:\n',nowa)
