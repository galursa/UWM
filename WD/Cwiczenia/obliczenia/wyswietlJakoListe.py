#Tworzymy funkcję, która będzie przyjmować dowolną ilość argumentów
#Funkcja będzie wyświetlać arguementy w postaci listy numerowanej

def wyswietlJakoListe(* elementy):
    dlugosc=len(elementy)
    if dlugosc==0:
        print("Brak elementów")
    else:
        for i in range(dlugosc):
            print(str(i+1)+'. '+str(elementy[i]))
