#funkcja, która bada ciąg arytmetyczny
#zwraca różnicę

def roznica_ciagu(* ciag):
    if len(ciag) == 0:
        return 0.0
    elif (ciag[0]!=0)&(len(ciag)==1):
        return ciag[0]
    else:
        roznica=ciag[1]-ciag[0]
        return roznica

print(roznica_ciagu(1,2,3,4))
