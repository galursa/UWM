import numpy as np
import matplotlib.pyplot as plt

# Top 5 najpopularniejszych języków programowania względem wyszukiwania
# na podstawie danych z
#https://mamstartup.pl/programowanie/10713/top-10-jezykow-programowania-z-najwyzszymi-zarobkami-w-2017

jezykipgr ={'java' : 17.3, 'C': 9.3, 'C++': 6.3, 'Python': 3.5, 'Visual Basci.Net' : 3.0}

# ustalamy liste kolorów, podajemy w wersji jak do html
kolory = ['#900050', '#FF0050', '#FF00FF', '#BB00AA', '#500050']

#Jeżeli chcemy, żeby wycinek z koła wyglądał jak wyjęty
#dodajemy wartości ułamkowe im większy ułamek tym bardziej "wyjęty" kawałek
kawalki = [0.3, 0, 0.1, 0, 0]

fig, ax = plt.subplots()
ax.axis('equal')        # żeby wykres kołowy był w kształcie koła

ax.pie(jezykipgr.values(), colors=kolory, shadow=True, startangle=60,
       explode=kawalki, labels=jezykipgr.keys(), autopct='%.1f%%',
       pctdistance=1.15, labeldistance=1.3)
plt.title('Popularność języków programowania')
plt.show()
