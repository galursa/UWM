import math

def row_kwadratowe(a, b, c):
    delta = b**2 - 4 * a * c
    if (delta < 0):
        print("Brak pierwiastków")
        return -1
    elif (delta == 0):
        print("Jeden pierwiastek")
        x = (-b) / (2 * a)
        return x
    else:
        print("Równanie ma dwa pierwiastki")
        x1= (- b - math.sqrt(delta)) / (2 * a)
        x2= (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))
