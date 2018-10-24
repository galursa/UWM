#wygenerujemy listę elementów podzielnych przez 4
#wykorzystując python comprehension

#wersja z petla
przez_4=[]
for x in range(10):
    przez_4.append(x*4)

print(przez_4)

#wersja python comprehension
przez_4_II=[x*4 for x in range(10)]

print(przez_4_II)
