with open('data.txt', 'r') as f:
    x = 12* [0]
    tot = 0
    for line in f.readlines():
        tot += 1
        for i, val in enumerate(line[:-1]):
            x[i] += (val=='1')
x = [y - tot//2>0 for y in x]
x.reverse()
print(sum((val*2**i for i, val in enumerate(x)))*sum(((not val)*2**i for i, val in enumerate(x))))
