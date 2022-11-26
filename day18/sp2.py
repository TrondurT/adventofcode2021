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
_tot_max = 0
_diff_max = 0
for i, x in enumerate(Data):
    for j, y in enumerate(Data):
        temp = (str2num(x)+str2num(y)).mag()
        _tot_max = max(_tot_max, temp)
        if i!=j:
            _diff_max = max(_diff_max, temp)
print(_tot_max)
print(_diff_max)
