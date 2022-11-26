with open('data.txt', 'r') as f:
    Data = [[int(x) for x in row[:-1]] for row in f.readlines()]

I, J = len(Data), len(Data[0])

tested = []
basins = []
for i in range(I):
    for j in range(J):
        to_test=[[i, j]]
        cur_basin=[]
        while to_test:
            cur_test = to_test.pop()
            if cur_test in tested:
                continue
            tested.append(cur_test)
            my_i, my_j = cur_test
            if Data[my_i][my_j] == 9:
                continue
            cur_basin.append([my_i, my_j])
            if my_i<I-1:
                to_test.append([my_i+1, my_j])
            if my_i>0:
                to_test.append([my_i-1, my_j])
            if my_j<J-1:
                to_test.append([my_i, my_j+1])
            if my_j>0:
                to_test.append([my_i, my_j-1])

        if cur_basin:
            basins.append(cur_basin)
x =[len(x) for x in basins]
x.sort()
prod = 1
for p in x[-3:]:
    prod *= p
print(prod)
