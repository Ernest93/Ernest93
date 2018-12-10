"""
8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
"""
liczba = input("Podaj liczbe ktorej chcesz sprawdzic podzielnosc przez 3 lub 5 lub 7: ")
liczba2 = int(liczba)
if(liczba2 % 3 == 0 or liczba2 % 5 == 0 or liczba2 % 7 == 0):
    print("Liczba jest podzielna przez 3 lub 5 lub 7")
else:
    print("Liczba nie jest podziela przez 3 lub 5 lub 7")