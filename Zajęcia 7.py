"""
import sys
import os
import send2trash

send2trash.send2trash("dane.txt")
os.chmod('')
#print(sys.path)
print(os.getcwd())
"""
"""
Program do zapisywania wpisow i ich przegladania

do menu proste printy
otwieranie pliku i przeczytanie go i zamkniecie
otwieranie pliku, zapis pliku i zamkniecie
otwieranie pliku przeczytanie usuniecie i zamkniecie
otwarcie pliku zapytanie o kryterium odnalezienie wpisu i zamkniecie
metoda exit konczy program

powtarzanie sie otwieranie, zamkniecie i odnalezienie wpisu wiec warto zrobic funkcje - 3 funkcje potrzebujemy i menu ktore rozpozna funkcje
"""
import pickle

def otworz_dziennik(plik_dziennika):
   dziennik = open(plik_dziennika, 'rb+')
   return dziennik

def zamknij_dziennik(plik_dz):
    plik_dz.close()

"""
lista ze słownikami ustawiamy, do rozkminienia jest, przekazywanie sobie parametrow do rozkminiecia(musze Myslec na zajecia sie przygotowywac!)
"""
def dodaj_wpis(plik_dz):
    data = input("Podaj datę: ")
    tresc = input("Podaj treść: ")
    nowy_wpis = {"data": data, "tresc": tresc}

    stare_wpisy = przeczytaj_plik(plik_dz)
    lista = []
    lista.append(stare_wpisy)
    lista.append(nowy_wpis)
    print(lista)
    pickle.dump(lista, plik_dz)

def wyswietl_menu():
    print("Mój dziennik v0.1\n"
          "1. Wyświetlanie\n"
          "2. Dodawanie\n"
          "3. Usuwanie\n"
          "4. Szukanie\n"
          "5. Wyjście")
def przeczytaj_plik(plik_dz):
    try:
     dane = pickle.load(plik_dz)
     print(dane)
     return dane
    except:
     print("Błąd")



def zapytaj():
    decyzja = input("Co wybierasz?")
    if decyzja == "1":
        print("Oto twoje wpisy:")
        plik_dz = otworz_dziennik(plik_dziennika)
        przeczytaj_plik(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "2":
        print("Dodawanie wpisu: ")
        plik_dz = otworz_dziennik(plik_dziennika)
        dodaj_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    elif decyzja == "5":
       exit()

plik_dziennika = 'dziennik.dz'
wyswietl_menu()
zapytaj()

while True:
      pass

