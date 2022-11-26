import numpy as np

data = np.loadtxt('data.txt')

_list1 = (sum(data[i:i+3]) for i in range(len(data)-2))
_list2 = (sum(data[i:i+3]) for i in range(len(data)-2))
next(_list2)
print(sum((j>i for i, j in zip(_list1, _list2))))
