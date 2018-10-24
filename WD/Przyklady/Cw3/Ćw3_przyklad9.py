#Mamy dwa rodzaje zmiennych: lokalne i globalne
#lokalne są widoczne tylko wewnątrz funkcji
#czyli po zakończeniu działania funkcji nie możemy się do nich dosać
#globalne są widoczne dla wszystkich procedur i funkcji
#Nie zaleca się jednak stosowania zmiennych globalnych
def dodaje():
    global a
    a=1
    b=3
    return a+b

def dodaje2():
    b=1
    return a+b

print(dodaje())
print(dodaje2())

