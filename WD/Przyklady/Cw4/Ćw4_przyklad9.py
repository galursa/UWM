class Ksztalty:
    #definicja zmiennej poprzedzonej __
    __jestemPrywatna__ = "xyz"
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
        self.x = self.y *czynnik


def zmieniamTekst(tekst):
    tekst+=" to jest to ;)"
    return tekst


#Tworzymy obiekt
kwadrat= Ksztalty(10,30)

#Sprawdzmy dostęp do zmiennej prywatnej
print(kwadrat.__jestemPrywatna__)

#a może uda nam się jeszcze zmienić wartość?
kwadrat.__jestemPrywatna__="na na na"
print(kwadrat.__jestemPrywatna__)

#spróbujmy czy nowa funkcja coś może zmienić
print(zmieniamTekst(kwadrat.__jestemPrywatna__))

