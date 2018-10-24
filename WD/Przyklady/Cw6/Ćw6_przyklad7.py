#importuje ElemenTree potrzebne do parsowania pliku XML
#w dalszej części pliku zamiast użwać długiej nazwy będziemy używać skrótu ET
from xml.etree import ElementTree as ET

#Ta funkcja pozwala sparsować dane z pliku xml na drzewo 'tree'
tree = ET.parse('data-text.xml')
#Do analizy danych porzebujemy ustawić się w korzeniu drzewa - zmienna 'root'
#Korzeniem drzewa jest pierwszy tag w pliku XML
root = tree.getroot()

data = root.find('Data')

#tworzymy pusty słownik, do którego będziemy dorzucać dane
all_data = []

for observation in data:
    record = {}
    for item in observation:
        
#Aby wyświetlić atrybuty wraz z kluczamy możemy uzyć komendy:
#        print(item.attrib.keys())
#Wykorzytamy ją do indeksowania danych:
#w Python 2.X wystarczy napisać:
#       lookup_key=item.attrib.keys()[0]

        lookup_key=list(item.attrib.keys())[0]
#Jeśli chcemy wyświetlić sprawdzany klucz:        
#        print(lookup_key)
        rec_key = item.attrib[lookup_key]
#jeśli chcemy wyświetlić klucze z rekordów:
        print(rec_key)

