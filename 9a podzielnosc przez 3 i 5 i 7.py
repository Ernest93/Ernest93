"""
9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
"""
liczba = input("Podaj liczbe ktorej chcesz sprawdzic podzielnosc przez 3 i 5 i 7: ")
liczba2 = int(liczba)
if(liczba2 % 3 == 0 and liczba2 % 5 == 0 and liczba2 % 7 == 0):
    print("Liczba jest podzielna przez 3 i 5 i 7")
else:
    print("Liczba nie jest podziela przez 3 i 5 i 7")