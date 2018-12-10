#To jest zwykły komentarz
#print("Takie linie się nie wykonują")

#zapisywanie do zmiennej
zmienna = "Ala ma kota"

#sprawdzanie typu
liczba_1_string = "1"
liczba_1_int = 1

print(type(liczba_1_int))
print(type(liczba_1_string))

#pobieranie danych od użytkownika i zmiana typu
wartosc_1 = input("Podaj licznbę 1: ")
wartosc_2 = input("Podaj licznbę 2: ")

#rzutowanie na liczbę: int(), lub ciąg znaków: str()
liczba_1 = int(wartosc_1)
liczba_2 = int(wartosc_2)

#operacje na różnych typach
print("Łączenie/konkatenacja:")
print(wartosc_1 + wartosc_2 * 3)
print("Dodawanie:")
print(liczba_1 + liczba_2)

#liczby zmiennoprzecinkowe
ulamek = 4.53
liczba_calkowita = 2

print(0.1 + 0.2)
print(ulamek * liczba_calkowita)

#instrukcje warunkowe
if liczba_1 > liczba_2:
  print("pierwsza jest większa")
else:
  print("druga chyba jest większa")