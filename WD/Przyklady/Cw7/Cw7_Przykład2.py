#importujemy odpowiedni moduł
import matplotlib.pyplot as plt
#z tego modułu wykorzystamy instrukcje linspace
import numpy as np

#generujemy x od -pi do pi
x =np.linspace(-np.pi, np.pi, 201)
#generujemy y pierwszej funkcji
y=[]
for liczba in x:
    y.append(np.cos(liczba))
#generujemy y drugiej funkcji
y1=[]
for liczba in x:
    y1.append(np.cos(2*liczba))

plt.figure(1)
plt.subplot(211)
plt.title('Wykres funkcji cos(x)')
plt.plot(x,y,'b-')
plt.xlabel('X')
plt.ylabel('Y')
plt.subplot(212)
plt.title('Wykres funkcji cos(2x)')
plt.plot(x,y1,'y--')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
