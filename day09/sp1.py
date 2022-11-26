with open('data.txt', 'r') as f:
    Data = [[int(x) for x in row[:-1]] for row in f.readlines()]

I,J = len(Data), len(Data[0])

cum_sum = 0

for i in range(I):

    if i==0:
        _is = [i+1]
    elif i==I-1:
        _is = [i-1]
    else:
        _is = [i-1, i+1]

    for j in range(J):

        if j==0:
            _js = [j+1]
        elif j==J-1:
            _js = [j-1]
        else:
            _js = [j-1, j+1]
        test_case = [[my_i, j] for my_i in _is] 
        test_case += [[i, my_j] for my_j in _js] 
        val = Data[i][j]
        _min = min((Data[my_i][my_j] for my_i, my_j in test_case))
        if val < _min:
            cum_sum += val+1
print(cum_sum)
