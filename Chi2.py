import numpy as np

np.set_printoptions(suppress=True)

with open('chi_data.txt') as f:
    lines = f.readlines()
    lines = [np.round(float(i), decimals=4) for i in lines]
    lines = np.sort(lines)

# def classes(n):
#     c = 1 + (3.3*np.log10(n))
#     return int(np.fix(c) + 1)

# def width(maximum, minimum, c):
#     return float(np.round((maximum-minimum)/c, decimals=4))


def intervals(c, w, minimum):
    arr = []
    aux = minimum
    for i in range(c):
        arr.append([aux, aux + w])
        aux = aux + w
    return np.round(arr, decimals=4)


def frequency(inter, lines, c, n):
    arr = [0]
    flag = 0
    aux = 0
    aux2 = 0

    for i in range(c):
        flag = 0
        while flag != 1:
            if (aux2 != n):
                if (inter[i][0] <= lines[aux2]) and (lines[aux2] <
                                                     inter[i][1]):
                    aux = aux + 1
                    arr[i] = aux
                    np.delete(lines, 0, 0)
                    aux2 = aux2 + 1
                else:
                    flag = 1
                    aux = 0
                    arr.append(0)
            else:
                arr.append(0)
                flag = 1
    return arr


n = len(lines)
c = 10
maximum = float(1.0000)
minimum = float(0.0000)
w = float(0.1000)
i = intervals(c, w, minimum)
f = frequency(i, lines, c, n)
E = 3.0000
VC = 16.9190

Test = []
for num in f:
    Test.append(((num - E)**2) / E)

Test.pop()
# calculate x^2
x_squared = sum(Test)
x_squared = round(x_squared, 4)

print("\nIntervals:    Observed     (O - E)^2 / E\n")
ziplist = [i, f, Test]
for x, y, Test in zip(*ziplist):
    print(str(x).strip("]"), ")", "      ", y, "       ", Test, "\n")

print('x^2=')
print(x_squared)

# interpret hipotesis value
print("\nThe hipotesis value is:")
if x_squared > VC:
    print(str(x_squared) + " > " + str(VC) + ", " + "H0 is rejected\n")
else:
    print(x_squared + " < " + VC + " ," + "H0 is accepted\n")
