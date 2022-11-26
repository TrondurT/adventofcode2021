with open('data.txt', 'r') as f:
    data = [[y for y in x[:-1]] for x in f.readlines()]
data2 = data.copy()

_len = len(data[0])

for i in range(_len):
    one = 0
    zero = 0
    for test in data:
        if test[i] == '1':
            one += 1
        else:
            zero += 1
    if len(data) == 1:
        break
    if one >= zero:
        data = [test for test in data if test[i] == '1']
    else:
        data = [test for test in data if test[i] != '1']
for i in range(_len):
    one = 0
    zero = 0
    for test in data2:
        if test[i] == '1':
            one += 1
        else:
            zero += 1
    if len(data2) == 1:
        break
    if one < zero:
        data2 = [test for test in data2 if test[i] == '1']
    else:
        data2 = [test for test in data2 if test[i] != '1']
data = [int(x) for x in data[0]]
data2 = [int(x) for x in data2[0]]
data.reverse()
data2.reverse()
print(sum((val*2**i for i, val in enumerate(data))) * sum((val*2**i for i, val in enumerate(data2))))
