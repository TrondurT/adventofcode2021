with open('data.txt', 'r') as f:
    Data = [
            [int(x) for x in row[:-1]]
            for row in f.readlines()
            ]


Data = [
            [
                (x+i+j-1) % 9+1
                for i in range(5)
                for x in row
            ]
        for j in range(5)
        for row in Data
        ]

to_try = [(0, 0)]
price = {(0, 0):0}
end = (len(Data)-1, len(Data[0])-1)

def find_min_edge():
    _min = 9999999
    _next = None
    for i, item in enumerate(to_try):
        if price[item]<_min:
            _min = price[item]
            _next = i
    return to_try.pop(_next), _min

def compare(y, x, val):
    if 0<=y<=end[0] and 0<=x<=end[1]:
        val += Data[y][x]
        if ((y, x) not in price) or val<price[(y, x)]:
                price[(y, x)] = val
                if (y, x) not in to_try:
                    to_try.append((y, x))

def test_nabors(edge, val):
    y, x = edge
    compare(y-1, x, val)
    compare(y+1, x, val)
    compare(y, x-1, val)
    compare(y, x+1, val)

while True:
    edge, val = find_min_edge()
    if edge == end:
        print(price[edge])
        break
    test_nabors(edge, val)
