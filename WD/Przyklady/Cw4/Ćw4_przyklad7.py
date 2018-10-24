class PierwszaKlasa:
    "Przykład klasy"
    atrybut = 54321
    def pierwszaMetoda(z):
        return "Teraz działa pierwsza Metoda"


obiekt = PierwszaKlasa()
print(obiekt)

#drukujemy atrybut
print(obiekt.atrybut)

#drukujemy metodę
print(obiekt.pierwszaMetoda())

#dodajemy atrybut do istniejącego obiektu
obiekt.tekst = "la la la"

print(obiekt.tekst)

#ale go nie będzie w nowej instancji klasy
nowyObiekt = PierwszaKlasa()
print(nowyObiekt.tekst)
