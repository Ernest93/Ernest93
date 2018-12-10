"""
#struktura słownika
slownik = {"imiona": [ "Łukasz", "Ala", "Ola", "mateusz","ernest"],"nazwiska": ["Falkowicz", "Kowalska", "Malinowska", "Igrekowski", "chojnacki"]}

miasta = {"miasta": ["Warszawa", "Gdańsk", "Sopot", "Kraków", "Berlin"]}

slownik.update(miasta)

miasta["panstwa"] = ["Polska","Polska","Polska","Polska","Niemcy"]

# Mam na imie XXXX nazwisko YYYY i mieszkam w ZZZZ
# Mam na imie XXXX nazwisko YYYY i mieszkam w ZZZZ
# Mam na imie XXXX nazwisko YYYY i mieszkam w ZZZZ

def wyswietl_slownik():
    for index, imie in enumerate(slownik["imiona"]):
        nazwisko = slownik["nazwiska"][index]
        miasto = miasta["miasta"][index]
        panstwo = miasta["panstwa"][index]
        print("Mam na imie: {} nazwisko: {} i mieszkam w miescie: {} a panstwo:  {}".format(imie, nazwisko,miasto,panstwo))

print("*" * 50)

wyswietl_slownik()

for klucz, wartosc in slownik.items():
    print(klucz)
    #print(wartosc)
    for index, dana in enumerate(wartosc):
        print("\t -> " + dana)

print("*" * 50)

# print(type(slownik))
# print(slownik)

# imiona:
#   -> Łukasz
#   -> Ala
#   -> Ola
# nazwiska:
#   -> Falkowicz
#   -> Kowalska
#   -> Malinowska

nazwiska = slownik["nazwiska"]
for dana in nazwiska:
    print("\t -> " + dana)

print("*" * 50)

def zwieksz_licznik(plik):
    plik = open(plik, "r+")
    licznik = int(plik.read())
    licznik += 1 # licznik = licznik + 1
    plik.seek(0)
    plik.write(str(licznik))
    print(licznik)
    plik.close()

zwieksz_licznik("dane.txt")

print("*" * 50)
"""
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
komentarz = input("Podaj komentarz: ")


with open("dane2.txt", "a+") as plik:
    plik.write(imie + "\t" + nazwisko + "\t" + komentarz + "\n")
    plik.seek(0)
    dane = plik.readlines()

for i, wpis in enumerate(dane):
    rozbite = wpis.split("\t") #ciekawostka, zachęcam do poczytania o medach dostępnych w list/dict/string są tam na prawde fajne smaczki :) Nie wymyślajmy koła na nowo.
    print("{:*^50}".format(" Wpis " +str(i+1)))
    print("Imie: {}, Nazwisko:, {}, Treść: {}".format(rozbite[0],rozbite[1],rozbite[2]), end='')