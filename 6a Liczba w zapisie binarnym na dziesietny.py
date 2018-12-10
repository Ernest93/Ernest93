"""
6. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny. Załóż że wpisywane
jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
"""
liczba_binarna = input("Podaj liczbe w zapisie binarnym o dlugosci 6 znakow: ")
liczba_dziesietna = ((int(liczba_binarna[0])*32) + (int(liczba_binarna[1])*16) + (int(liczba_binarna[2])*8) +
(int(liczba_binarna[3])*4) + (int(liczba_binarna[4])*2) + (int(liczba_binarna[5])*1))
print("Podana liczba w zapisie binarym o dlugosci znakow 6 wynosi: " + str(liczba_dziesietna) + " w zapisie dziesietnym")