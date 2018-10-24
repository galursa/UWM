#Zagnieżdżanie
#Zamiast pisać tak:
lista=[]
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
      if i != j:
          lista.append((i,j))
print(lista)

#można to zrobić krócej
lista2=[(i,j) for i in [1, 2, 3] for j in [4, 5, 6]]
print(lista2)
        
