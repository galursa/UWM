#pliki możemy otwierać do odczytu i zapisu za pomocą komendy with
#wówczas nie musimy się martwić o zamykanie pliku

#Pętla for pozawala na wyświetlenie pliku linijka po linijce
with open("dane.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
