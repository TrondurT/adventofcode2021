from number import Number

with open('data.txt') as f:
    Data = [x.strip() for x in f.readlines()]

def str2num(temp):
    arr = []
    i = [arr]
    for l in temp[1:]:
        if l =='[':
            newarr = []
            i[-1].append(newarr)
            i.append(newarr)
        elif l in '0123456789':
            i[-1].append(int(l))
            state = 'd'
        elif l == ',':
            pass
        elif l == ']':
            i.pop()
        else:
            raise Exception
    return Number(arr)

a = str2num(Data[0])
s = sum([str2num(x) for x in Data[1:]], start=a)
print(s.mag())
