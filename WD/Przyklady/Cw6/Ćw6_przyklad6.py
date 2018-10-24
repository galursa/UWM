#importuje ElemenTree potrzebne do parsowania pliku XML
#w dalszej części pliku zamiast użwać długiej nazwy będziemy używać skrótu ET
from xml.etree import ElementTree as ET

#Ta funkcja pozwala sparsować dane z pliku xml na drzewo 'tree'
tree = ET.parse('data-text.xml')
#Do analizy danych porzebujemy ustawić się w korzeniu drzewa - zmienna 'root'
#Korzeniem drzewa jest pierwszy tag w pliku XML
root = tree.getroot()

data = root.find('Data')

#tworzymy pustą liste, do której będziemy dorzucać dane
all_data = []

for observation in data:
    record = {}
    for item in observation:
#Sprawdzcie co się stanie gdy zamienimy item na item.text a potem na list(item)
        print(item)
#Atrybuty wyświetlą się gdy w miejsce print(item) wpiszemy
#        print(item.attrib)
