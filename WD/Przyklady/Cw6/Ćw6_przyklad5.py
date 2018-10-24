#importuje ElemenTree potrzebne do parsowania pliku XML
#w dalszej części pliku zamiast użwać długiej nazwy będziemy używać skrótu ET
from xml.etree import ElementTree as ET

#Ta funkcja pozwala sparsować dane z pliku xml na drzewo 'tree'
tree = ET.parse('data-text.xml')
#Do analizy danych porzebujemy ustawić się w korzeniu drzewa zmienna 'root'
#Korzeniem drzewa jest pierwszy tag w pliku XML
root = tree.getroot()

#komenda pozwoli wydrukować korzeń drzewa z pliku XML
print(root)

#pozwala na wyświetlenie elementów składowych względem korzenia
print(list(root))

