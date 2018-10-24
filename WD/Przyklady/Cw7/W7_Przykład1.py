#importujemy odpowiedni moduł z nazwą skróconą plt
import matplotlib.pyplot as plt

#Tworzymy tablicę x i tablicę y
x=[-4,-3,-2,-1,0,1,2,3,4]
y=x

#Ponizsze 3 komendy sa podobne do matlabowych
# Plot rysuje, xlabel i ylabel nadaja nazwy dla etykiet

plt.plot(x,y,'ro-')
plt.xlabel('X')
plt.ylabel('Y')


# show pokazuje rysunek
plt.show()
