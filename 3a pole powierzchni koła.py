"""
3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu
"""
import math
Pi = math.pi
promien = input("Podaj wartość promienia koła: ")
Pole_koła = Pi*int(promien)*int(promien)
print("Pole koła o zadanym promieniu wynosi: " + str(Pole_koła))