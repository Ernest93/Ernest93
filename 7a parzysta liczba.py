"""
7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.
"""
liczba = input("Podaj liczbe ktorej chcesz sprawdzic parzystosc: ")
liczba2 = int(liczba)
if(liczba2 % 2 == 0):
    print("Liczba jest podzielna przez 2")
else:
    print("Liczba nie jest podziela przez 2")