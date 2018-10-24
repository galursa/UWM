a=input("Proszę podać pierwszą liczbę \n")
b=input("Proszę podać druga liczbę \n")
c=input("Proszę podać trzecia liczbę \n")
a=int(a)
b=int(b)
c=int(c)

if (a in range(11))&((a>b)|(b>c)):
    print("a zawiera sie w przedziale (0,10>\n i a jest większe od b lub b jest większe od c")
else:
    print("a nie spełania warunków \n")
