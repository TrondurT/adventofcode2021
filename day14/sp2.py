def recersive(ind):
    if ind in cache:
        return cache[ind]
    _int = int(ind[2:])
    temp = bace_dict.copy()
    if _int == 1:
        temp[rules[ind[:2]]]+=1
        cache[ind] = temp
        return temp
    new_item = rules[ind[:2]] 
    temp[new_item]+=1
    add_dict(temp, recersive(ind[0]+new_item+str(_int-1)))
    add_dict(temp, recersive(new_item+ind[1]+str(_int-1)))
    cache[ind] = temp
    return temp


def add_dict(a, b):
    for key in a:
        a[key] += b[key]

def start_process(arr):
    _dict = bace_dict.copy()
    old = arr.pop(0)
    _dict[old]+=1
    while arr:
        new = arr.pop(0)
        _dict[new]+=1
        add_dict(_dict, recersive(old+new+str(40)))
        old = new
    return _dict

with open('data.txt') as f:
    start = f.readline()[:-1]
    f.readline()
    rules = {
            x[0]:x[1] 
            for x in [
                y[:-1].split(' -> ')
                for y in f.readlines()
                ]
            }

string = [a for a in start]
all_letters = set(string + list(rules.values()))
bace_dict = {a:0 for a in all_letters}
cache = {}

_dict = start_process(string)
_list = list(_dict.values())
_list.sort()

print(_list[-1]-_list[0])

