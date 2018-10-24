def iloczyn_ciagu(* ciag):
    if len(ciag) == 0:
        return 0.0
    else:
        iloczyn=1.0
        for elem in ciag:
            #iloczyn = iloczyn*elem
            iloczyn*=elem
        return iloczyn


print(iloczyn_ciagu())
print(iloczyn_ciagu(1, 2, 3, 4))
print(iloczyn_ciagu(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
