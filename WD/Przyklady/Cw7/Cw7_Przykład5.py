#importujemy odpowiedni moduł
import matplotlib.pyplot as plt
#z tego modułu wykorzystamy instrukcje linspace
import numpy as np

#generujemy liczby losowe
#informacje o random można uzyskać pod
#https://docs.scipy.org/doc/numpy/reference/routines.random.html
x = np.random.normal(size=100)
#generujemy histogram z danych
n, bins, patches = plt.hist(x)
#Dodajemy tytuł i etykiety
plt.title('Wykres losowy elementów')
plt.xlabel('Wartośc ')
plt.ylabel('Prawdopodobieństwo')
#Ustawiamy zakres dla poszczególnych osi
#[xmin, xmax, ymin, ymax]
plt.axis([-4, 4, 0, 30])
#Ustawienie widoczności siatki
plt.grid(True)
plt.show()
