import xlrd

# otwarcie pliku
book = xlrd.open_workbook("DaneExcel.xlsx")

# dla każdego arkusza wyświetlamy zawartość pola 0,0
for sheet_name in book.sheet_names():
	arkusz = book.sheet_by_name(sheet_name)
	print(arkusz.row_values(0)[1])

# drukujemy liczbę akruszy
print(book.nsheets)

# drukujemy nazwę akruszy
print(book.sheet_names())
 
#bierzemy pierwszy akrusz w nawiasach jest podany numer do niego
first_sheet = book.sheet_by_index(0)

#Odczytujemy wiersz
print(first_sheet.row_values(0))

#Odczytujemy pierwszą komórkę i ją wyświetlamy.
cell = first_sheet.cell(0,0)
print(cell)
print(cell.value)
 
#Odczytuje pierwszy wiersz (rowx) zaczynając od kolumny 0 (start_colx)
#kończąc na kolumnie 2 (end_colx)
print(first_sheet.row_slice(rowx=3,
                                start_colx=0,
                                end_colx=2))
 
#drukujemy wszystkie wiersze z danego arkusza
#tutaj z arkusza pierwszego
for i in range(first_sheet.nrows):
    print(first_sheet.row_values(i))
