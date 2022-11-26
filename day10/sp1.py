with open('data.txt') as f:
    Data = [x[:-1] for x in f.readlines()]

_dict = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>'
        }

score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }

temp = Data[0]
stack = []
cum_sum = 0
for temp in Data:
    for car in temp:
        if car in '([{<':
            stack.append(car)
        else:
            match = stack.pop()
            if _dict[match] != car:
                cum_sum += score[car]
                break
print(cum_sum)
