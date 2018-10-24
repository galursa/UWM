#Chcemy napisać funkcję, która generuje liczby
#które są wielokrotnością 4
#Wykorzystamy Python Comprehension

def wielokrotnosc4(ile):
    liczby=[x for x in range(4,(ile+1)*4,4) ]
    return liczby

