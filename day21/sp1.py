with open('data.txt', 'r') as f:
    data = {}
    for i, d in enumerate(f):
        # teir eru á felt eitt minni enn teir eru á
        data[i] = int(d.split(':')[1].strip())-1

def dice():
    n = 0
    while True:
        _list = []
        for _ in range(3):
            _list.append(n+1)
            n = (n+1)%100
        yield sum(_list)

roll = dice()

pl = 0
sc = {0:0, 1:0}

N = 0
for roll in dice():
    N+=3
    data[pl] = (data[pl] + roll)%10
    sc[pl] += data[pl] +1
    if sc[pl]>=1000:
        print(sc[pl+1%2]*N)
        break
    pl = (pl+1)%2

