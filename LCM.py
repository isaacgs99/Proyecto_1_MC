import numpy as np
np.set_printoptions(suppress=True)

# X0 = 6, a = 32, c = 3, m = 80

print("METODO LINEAL CONGRUENCIAL\n")

x0 = input("X0 = ")
x0 = int(x0)
a = input("a = ")
a = int(a)
c = input("c = ")
c = int(c)
m = input("m = ")
m = int(m)
cycles = input("ciclos = ")
cycles = int(cycles)

r = np.arange(cycles)

for i in range(cycles):
    x0 = (a*(x0) + c) % m
    r = np.append(r, x0/m)

print("RESULTADO: \n")
print(r)
