with open('data.txt', 'r') as f:
    data = []
    for line in f:
        row = []
        data.append(row)
        sp = line.strip().split()
        row.append(sp[0]=='on')
        for st in sp[1].split(','):
            temp = [int(x) for x in st.split('=')[1].split('..')]
            if temp[1]<temp[0]:
                raise Exception
            row.append(temp)

_set = set()

for row in data:
    if row[0]:
        op = _set.add
    else:
        op = _set.discard
    for x in range(max(-50, row[1][0]), min(50, row[1][1]+1)):
        for y in range(max(-50, row[2][0]), min(50, row[2][1]+1)):
            for z in range(max(-50, row[3][0]), min(50, row[3][1]+1)):
                op((x, y, z))
print(len(_set))

