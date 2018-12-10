##praca z modułem csv
import csv

baza_adresowa = 'adresy.csv'

with open(baza_adresowa) as plik:
    reader = csv.reader(plik)

    lista_slownikow = []
    dane = list(reader)
    klucze = dane.pop(0)

    for wiersz in dane:
        slownik = {}
        for i, kolumna in enumerate(wiersz):
             klucz = klucze[i]
             slownik[klucz] = kolumna

        lista_slownikow.append(slownik)

for wiersz in lista_slownikow:
    print("Osoba: {osoba[Imie]} ma numer telefonu: {osoba[Telefon]}".format(osoba = wiersz))

## Praca z modułem pickle
import pickle

lista = [1, 2, 3, 4]
file = open('dane.save', 'wb')
pickle.dump(lista, file)
file.close()

file = open('dane.save', 'rb')
print (pickle.load(file))
file.seek(0)
print(type(pickle.load(file)))
file.close()