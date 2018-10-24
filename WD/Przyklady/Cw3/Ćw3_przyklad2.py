#Chcemy uzyskać liczby parzyste z podanego zakresu

#Wersja z pętlą

liczby=[1,2,3,4,5,6,7,8,9,10]
lista=[]
for i in liczby:
    if i % 2 == 0:
        lista.append(i)

print("Liczby parzyste uzyskane z wykorystaniem pętli")
print(lista)

#wersja z Python comprehension

lista2=[i for i in liczby if i % 2 == 0]
print(lista2)
