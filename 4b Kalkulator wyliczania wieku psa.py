"""
4) Kalkulator do wyliczania wieku psa.
   Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
   Np: 15 ludzkich lat to 73 psie lata
"""

wiekpsa = input("Ile lat ma pies? :")
wiek = int(wiekpsa)
if wiek <=2:
    print("Pies ma" + str(wiek*10.5) + "ludzkich lat")
else:
    print("Pies ma " + str((wiek*4)+13) + " ludzkich lat")