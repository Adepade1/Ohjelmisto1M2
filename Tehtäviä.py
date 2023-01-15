import math
import random


# 1.

print("Terve,",input("Anna nimesi: "))


input("")


# 2.

Radius = int(input("Syötä säde: "))
Circumference = math.pi*Radius**2

print("Ympyrän pinta-ala: ",Circumference)


# 3.

Base = float(input("Anna kanta:\n"))
Height = float(input("Anna korkeus:\n"))

Perimeter = 2 * (Base + Height)
Area = (Height * Base / 2)

print("Suorakulmion piiri on ", Perimeter)
print("Suorakulmion pinta-ala on ", Area)



# 4.

print()

Numbers = {
    float(input("Anna 3 lukua\n")),
    float(input()),
    float(input()),
}

Summa = sum(Numbers)
Tulo = 1
Keskiarvo = 0

for Num in Numbers:
    Keskiarvo += Num
Keskiarvo /= len(Numbers)

for Num in Numbers:
    Tulo *= Num

print(Summa)
print(Tulo)
print(Keskiarvo)


# 5.

print()

def GramToKilogram(Grams):
    return Grams*0.001

Leivaska = float(input("Anna leiväskät:\t"))
Naula = float(input("Anna naulat:\t"))
Luoti = float(input("Anna luodit:\t"))

NaulaPaino = Leivaska * 20 + Naula
LuotiPaino = NaulaPaino * 32 +Luoti
Paino = LuotiPaino * 13.3


print("\nGrammoina: ", int(Paino%1000))
print("Kilogrammoina: ", int(GramToKilogram(Paino)))


# 6.

print("\n Kolminumerinen Koodi:")

ThreeNumCode = {}

ThreeNumCode[2] = 3

for i in range(3):
    ThreeNumCode[i] = random.randint(0,9)
    print(ThreeNumCode[i])

print("\n Nelinumerinen Koodi:")

FourNumCode = {}

for i in range(4):
    FourNumCode[i] = random.randint(1,6)
    print(FourNumCode[i])
