#Generujemy zbior liczb postaci 1/x, gdzie x jest całkowite z przedziału(0,9]
#Do tego celu zdefiniujemy funkcję

def JedenPrzezX():
    Zbior = [1/x for x in range(1,10)]
    return Zbior


print(JedenPrzezX())
