"""
10. Napisz program do sprawdzenia czy podany rok jest rokiem przestępnym
"""
rok = input("Podaj rok: ")
rok2 = int(rok)
if(rok2 % 4 == 0 and rok2 % 100 != 0):
    print("Rok jest przestępny")
elif(rok2 % 4 == 0 and rok2 % 100 ==0 and rok2 % 400 == 0):
    print("Rok jest przestępny")
else:
    print("Rok nie jest przestępny")