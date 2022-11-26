import numpy as np

data = np.loadtxt('data.txt')

count = 0
for i, j in zip(data[:-1], data[1:]):
    count += (j>i)
print(count)
