from cmath import sqrt

printNumbers = input(
    "Do you want to print all numbers and generated signs (y/n) :")

file1 = open('runs_data.txt', 'r')
Lines = file1.readlines()
numbers = []

# Importamos los números del documento
for line in Lines:
    numberToAdd = float(line)
    numbers.append(numberToAdd)

# Generamos los signos
generatedSigns = []

for x in range(len(numbers) - 1):
    if (numbers[x]) < (numbers[x+1]):
        generatedSigns.append("+")
    else:
        generatedSigns.append("-")

# Generamos el número de rachas
numberOfRates = 0

for x in range(len(generatedSigns)-1):
    if generatedSigns[x] != generatedSigns[+1]:
        numberOfRates = numberOfRates+1

# Generamos los datos estadísticos

miu = (2*(len(generatedSigns))-1)/3
sigmaSquared = round((16*(len(generatedSigns))-29)/90, 5)
sigma = sqrt(sigmaSquared)

z = (numberOfRates-miu)/sigma

# Imprimimos los datos obtenidos y un resumen de todas las operaciones
if printNumbers == "y":
    print("Number list")
    print(numbers)

print("\n")
print(f"Total of numbers: {len(numbers)} \n")
print(f"Total signs: {len(numbers)-1} \n")
print(f"Total runs: {numberOfRates} \n")

if printNumbers == "y":
    print("Signs generated")
    print(generatedSigns)
print("\n")
print("Statistics")
print(f"miu: {miu}")
print(f"sigmaSquared: {sigmaSquared}")
print(f"sigma: {sigma}")
print(f"z: {z}")
print("\n")
print("Hypothesis")
print("H0: Appearance of the numbers is random")
print("H1: Appearance of the numbers is not random")

if (abs(z) < 1.96):
    print(f"Since |{z}| < |1.96|, H0 is not rejected")
else:
    print(f"Since |{z}| > |1.96|, H1 is not rejected")
