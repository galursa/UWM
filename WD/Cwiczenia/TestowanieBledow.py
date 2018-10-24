try:
    zmienna=input("Proszę podać liczbę")
    print(zmienna)
    zmienna=int(zmienna)
    zmienna*=2
    print(zmienna+":")
except TypeError:
    print("Powstał błąd rzutowania typu")
