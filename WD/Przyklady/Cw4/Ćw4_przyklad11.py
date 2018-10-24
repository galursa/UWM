class Pieniadze:
    def __init__(self, rodzaj):
        self.rodzaj=rodzaj #banknot, moneta
    

class Wartosc:
    def __init__(self, wartosc, jednostka):
        self.wartosc=wartosc #
        self.jednostka=jednostka


class Monety(Pieniadze):
    def __init__(self,waluta):
        self.waluta=waluta
    


print("inicjujemy klasę Monety")
zlotowka=Monety('PLN')
z=zlotowka.waluta
print(zlotowka.waluta)
zlotowka.wartosc=1
print(zlotowka.wartosc)
zlotowka.rodzaj='moneta'
print(zlotowka.rodzaj)


