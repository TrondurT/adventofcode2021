with open('data.txt') as f:
    Data = [x[:-1] for x in f.readlines()]

_dict = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>'
        }

score = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
        }

temp = Data[0]
values = []
for temp in Data:
    stack = []
    flag = False
    for car in temp:
        if car in '([{<':
            stack.append(car)
        else:
            match = stack.pop()
            if _dict[match] != car:
                flag = True
                break
    if flag:
        continue
    cum_sum = 0
    while stack:
        cum_sum = 5*cum_sum + score[stack.pop()]
    values.append(cum_sum)
values.sort()
print(values[len(values)//2])
