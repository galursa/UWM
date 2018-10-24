class Ksztalty:
    #definicja konstruktora
    def __init__(self, x, y):
        #deklarujemy atrybuty
        #self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def poleProstokatu(self):
        return self.x*self.y

    def obwod(self):
        return 2*self.x +2*self.y

    def dodajOpis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x *czynnik
        self.y = self.y *czynnik


#a teraz klasa która dziedziczy po klasie Ksztalty
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x

#i jeszcze klasa, która dziedziczy po klasie Kwadrat
#bedzie definiwoać figurę złożoną z 3 kwadratów w kształcie litery L
# _
#| |_
#|_ _| 
class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        return 8*self.x

    def poleProstokatu(self):
        return 3*self.x*self.y

print("inicjujemy klasę Kwadrat")
figura = Kwadrat(5)

#sprawdzamy metody z klasy bazowej
print(figura.poleProstokatu())

print(figura.obwod())

figura.dodajOpis("Kwadrat")

print(figura.opis)

figura.skalowanie(0.3)

print(figura.obwod())

print("inicjujemy klasę KwadratowaLiteraL")
literaL=KwadratowaLiteraL(5)

#sprawdzamy jakie możemy wywołać metody
print(literaL.obwod())
print(literaL.poleProstokatu())
literaL.dodajOpis("Litera L")
print(literaL.opis)
literaL.skalowanie(0.5)
print(literaL.obwod())
