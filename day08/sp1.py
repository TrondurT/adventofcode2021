def by_len(ind:str):
    a = len(ind)
    if a in [2, 3, 4, 7]:
        return 1
    return 0

with open('data.txt', 'r') as f:
    data = [x[:-1].split('|')[1].split() for x in f.readlines()]
print(sum([sum([by_len(x) for x in line]) for line in data]))
