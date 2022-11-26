with open('data.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]

m=99999999999
for i in range(max(data)):
    m = min(sum([abs(x-i)*(abs(x-i)+1)/2 for x in data]), m)
print(int(m))
