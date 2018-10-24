#importujemy odpowiedni moduł
import matplotlib.pyplot as plt

#aby narysowac wykres potrzebujemy dwóch tablic liczb: x i y
#y to będzie tablica z wartościami funkcji x**2
#w zakresie do petli sa podane wartosci
#w petli obliczone elementy dorzucamy do listy
#mozna tez napisac y.append(liczba**2)
x=[-4,-3,-2,-1,0,1,2,3,4]
y=[]

for liczba in x:
    y+=[liczba**2]


#Ponizsze 3 komendy sa podobne do matlabowych
# Plot rysuje, xlabel i ylabel nadaja nazwy dla etykiet

plt.plot(y)
plt.xlabel('X')
plt.ylabel('Y')


#jeśli chcemy narysowac jeszcze jeden wykres o innych kolorach
y1=[]
for liczba in x:
    y1+=[liczba**2+1]

plt.plot(x,y1,'ro-')

# show pokazuje rysunek
plt.show()
