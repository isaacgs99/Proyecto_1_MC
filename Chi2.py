import numpy as np

np.set_printoptions(suppress=True)

with open('chi_data.txt') as f:
    lines = f.readlines()
    lines = [np.round(float(i), decimals=4) for i in lines]
    lines = np.sort(lines)
