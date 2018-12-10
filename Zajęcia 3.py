"""
#escapowanie znaków specjlanych

zmienna = r"To jest jakiś \ntekst z użytym znakiem nowej lini który ni będzie interpretowany"
print(zmienna)

zmienna = 'To jest jakiś: "tekst" z użytym cudzysłowem'
print(zmienna)

zmienna = 'To jest \n nowa linia'
print(zmienna)
"""
#kilka sposobów na formatowanie stringów
"""
wartosc_zmiennej = 23
zmienna = f"To jest napis: {wartosc_zmiennej}" #nie trzeba martiwć się rzutowaniem
print(zmienna)

zmienna = "To jest napis: " + str(wartosc_zmiennej)
print(zmienna)

zmienna = 012.33001
print("zmienna %s" % zmienna)
print("zmienna %f" % zmienna)
print("zmienna %d" % zmienna)

#więcej o stringach https://docs.python.org/3/tutorial/introduction.html#strings
#inne ciekawe znaczniki formatowania https://docs.python.org/3/library/string.html#format-examples

print("To jest {ilosc} sposób na wprowadzanie {nazwa}".format(nazwa='zmiennych', ilosc=3))

#sprawdzanie wielu warunków
"""
""""

liczba = 13456

if(liczba % 3 == 0 and liczba % 5 == 0):
    print("liczba podzielna przez 3 i 5")
elif(liczba % 3 == 0 or liczba % 5 == 0):
    print("liczba podzielna przez 3 lub 5")
elif(liczba % 3 == 0):
    print("liczba podzielna przez 3")
elif(liczba % 5 == 0):
    print("liczba podzielna przez 5")
else:
    print("nie podzielna przez 3 i 5")

"""
""""
#tworzenie obiektu typu range()
duzy_zakres = range(1,40000000)

lista = [1, 2, "trzy", 4, "pięć"]
print(lista)

#nadpisywanie wartości
lista[0] = "jeden"
lista[0] = "1"
lista[0] = "raz"

#dodawanie na koniec listy
lista.append("sześć")

#kasowanie na podstawie indeksu
del(lista[0])

#kasowanie na podstawie wartości
print(lista.remove("trzy")) #sprawdźcie co się stanie jak podamy wartość której nie ma

#zrzucanie elementu
print(lista.pop(2))

#inne ciekawe fukncje https://docs.python.org/3/tutorial/datastructures.html#more-on-lists


duza_lista = list(range(1,50))

#ogromna_lista = list(range(1,40000000)) #może "zabić" komputer ;)

#listy zagnieżdżone
lista_2d = [
    [1,2,3],
    [4,5,6, "NAPIS"],
    [7,8,9]
]

lista_2d[1][3] = lista_2d[1][3] + '!!!!'
print(lista_2d)

#rozpakowywanie
wyrazy = ("raz", "dwa", "trzy")
a, b, c = wyrazy
"""

print("Policzę dla ciebie do 100")
i=1
while (i <= 100):
    print(str(i)  + ' ', end='') # print bez nowych linii
    # print(i)
    i += 1

print('\nA teraz Cię o coś zapytam')
print('=' * 20) #mnożenie stringów

#pętla przydatna przy odpytywaniu użytkownika o coś
decyzja = None
while(decyzja != 'T'):
    decyzja = input("Wcisnij 'T' aby zakonczyc program: ")