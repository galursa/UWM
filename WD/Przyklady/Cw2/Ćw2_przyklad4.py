#Szukamy największego elementu

l=input("Podaj pierwszą liczbę")
k=input("Podaj drugą liczbę")
c=input("Podaj trzecią liczbę")
#l, k są typu string musimy ją rzutować na całkowitą

l=int(l)
k=int(k)
c=int(c)
#przy wyświetlaniu zmieniamy liczbę na typ string

if (l > k)&(l>c):
    print("Liczba="+str(l)+" jest większa")
elif (k > l)&(k>c):
    print("Liczba="+str(k)+" jest większa")
elif (c > l)&(c>k):
    print("Liczba="+str(c)+" jest większa")
