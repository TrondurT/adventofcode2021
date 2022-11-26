with open('data.txt', 'r') as f:
    Data = [x[:-1] for x in f.readlines()]

points = []
folds = []
for i, item in enumerate(Data):
    if item:
        points.append([int(x) for x in item.split(',')])
    else:
        break
for i in range(i+1, len(Data)):
    fold = Data[i].split()[-1].split('=')
    fold[1] = int(fold[1])
    folds.append(fold)

xmax = max([x[0] for x in points])
ymax = max([x[1] for x in points])

def fold_fun(ori, pos):
    global xmax, ymax
    if ori == 'x':
        ori=0
        xmax = pos-1
    elif ori == 'y':
        ori=1
        ymax = pos-1
    for item in points:
        if item[ori]>pos:
            item[ori] = 2*pos - item[ori]
    return xmax, ymax

for fold in folds:
    fold_fun(*fold)
    arr = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]
    for x, y in points:
        arr[y][x] = 1
    print(sum((sum((x for x in row)) for row in arr)))
    break
