#wygenerować listę liczb podzielnych przez 6

#wersja z pętlą
podziel_przez_6 =[]
for elem in range(10):
    podziel_przez_6.append(elem*6)

print(podziel_przez_6)

#wersja z python comprehension
podziel_przez_6_II=[elem*6 for elem in range(10)]
print(podziel_przez_6_II)
