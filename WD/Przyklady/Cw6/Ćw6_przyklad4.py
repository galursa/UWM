#biblioteka potrzebna do obsługi plików json
import json

#w nawiasie podajemy nazwę naszego pliku
#funkcja read() odczytuje plik a wszystko zapisuje się pod zmienną json_plik
json_plik = open('data-text.json').read()
#json.loads zapisuje dane z pliku json_plik do zmiennej data
data = json.loads(json_plik)

#wyświetlamy informacje na ekran
for item in data:
    print(item)
