# ** czyli dwie gwiazdki oznaczają że możemy użyć 
# dowolną ilość argumentów z kluczem
def to_lubie(** rzeczy):
    for cos in rzeczy:
        print("To jest ")
        print(cos)
        print(" co lubie ")
        print(rzeczy[cos])


to_lubie(slodycze="czekolada", rozrywka=["disco-polo", "moda na sukces"])
