plik = open('file.txt')
try:
    tekst = plik.read()
finally:
    plik.close()

data = tekst.split(" ")
num_of_char = len(data)
print('Count in text file :', num_of_char)