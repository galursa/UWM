#importujemy odpowiedni moduł
import matplotlib.pyplot as plt
#z tego modułu wykorzystamy instrukcje linspace
import numpy as np

#generujemy x 
x =np.linspace(-5, 5, 20)
#generujemy y pierwszej funkcji
y=[]
for liczba in x:
    y.append(liczba)
#generujemy y drugiej funkcji
y1=[]
for liczba in x:
    y1.append(3*liczba+2)
#generujemy y trzeciej funkcji
y2=[]
for liczba in x:
    y2.append(4*liczba+1)
#przygotowanie miejsca do rysowania z legendami
fig, ax = plt.subplots()
#plt.figure(1)
plt.title('Wykres funkcji y=ax+b')
ax.plot(x,y,'b-',label="y=x")
ax.plot(x,y1,'y--',label="y=3x+2")
ax.plot(x,y2,'r-.',label="y=4x+1")
plt.xlabel('X')
plt.ylabel('Y')
#ustalanie gdzie legenda ma być widoczna i jakie ma miec parametry
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#Dodanie koloru tła
legend.get_frame().set_facecolor('#55FF55')

plt.show()
