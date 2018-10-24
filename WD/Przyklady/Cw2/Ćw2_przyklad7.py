import sys

for i in [1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5]:
        #sprawdza czy jest w pionowej linii H
        if i==3: 
            sys.stdout.write('H')
        #jeśli nie to rysuje H na brzegach
        else:
            #sprawdzamy czy j zawiera się na liście, czyli jest na brzegach
            if j in [1,5]: 
                sys.stdout.write('H')
            #jeśli nie piszemy spację
            else:
                sys.stdout.write(' ')
    sys.stdout.write('\n')
