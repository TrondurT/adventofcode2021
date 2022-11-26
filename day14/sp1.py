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
for _ in range(10):
    build = [string.pop(0)]
    while string:
        temp = string.pop(0)
        build.append(rules[build[-1]+temp])
        build.append(temp)
    string = build

_dict = {}
for letter in ''.join(string):
    if letter in _dict:
        _dict[letter] += 1
    else:
        _dict[letter] = 0
_list = list(_dict.values())
_list.sort()
print(_list[-1]-_list[0])

