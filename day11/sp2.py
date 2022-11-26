with open('data.txt', 'r') as f:
    Data = [[int(x) for x in row[:-1]] for row in f.readlines()]

I, J = len(Data), len(Data[0])
def find_nine(data):
    out = []
    for i in range(I):
        for j in range(J):
            if data[i][j] >9:
                out.append([i, j])
    return out

for step in range(1200):
    for i in range(I):
        for j in range(J):
            Data[i][j] += 1
    step2 = True
    flashis = []
    while step2:
        step2 = False
        for i, j in find_nine(Data):
            if [i, j] in flashis:
                Data[i][j] = -99
                continue
            flashis.append([i, j])
            step2 = True

            _is = [i]
            if i>0:
                _is.append(i-1)
            if i<I-1:
                _is.append(i+1)
            _js = [j]
            if j>0:
                _js.append(j-1)
            if j<J-1:
                _js.append(j+1)

            for my_i in _is:
                for my_j in _js:
                    Data[my_i][my_j] += 1
    if len(flashis) == I*J:
        break
    for i, j in flashis:
        Data[i][j] = 0
print(step+1)
