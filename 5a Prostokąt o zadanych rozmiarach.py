"""
5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
    | (bok)
    - (góra/dół)
    + (wierzchołek)
"""
boka = input("Podaj wysokość: ")
bokb = input("Podaj szerokość: ")
print("+" + ('-\t' * int(bokb))+ "+")
print(("|" + (("\t") * int(bokb))+"|\n")*int(boka))
print("+" + ('-\t' * int(bokb))+"+")