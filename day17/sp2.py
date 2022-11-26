with open('data.txt', 'r') as f:
    x, y = [z.split('=')[1].replace(',', '').split('..')
            for z in f.read().strip().split()[-2:]]
    x_bound = [int(z) for z in x]
    y_bound = [int(z) for z in y]

x0 = 0
y0 = 0

x = 7
y = 0

pos_steps = {}
_list_end_ind = []

for x in range(x_bound[1]+1):
    x_init = x
    x0 = 0
    step = 0
    end_ind = False
    while x0<x_bound[1] and x>0:
        step +=1
        x0 += x
        x = max(x-1, 0)
        if x_bound[0]<=x0<=x_bound[1]:
            if step not in pos_steps:
                pos_steps[step] = []
            pos_steps[step].append(x_init)
    if x_bound[0]<=x0<=x_bound[1] and x==0:
        _list_end_ind.append(x_init)

max_step = max(pos_steps.keys())
for fill in _list_end_ind:
    for step in range(1, max_step+1):
        if fill in pos_steps[step]:
            break
    for step in range(step+1, max_step+1):
        if fill not in pos_steps[step]:
            pos_steps[step].append(fill)

count = 0
y_init = 0
_max = 0
y_hit = []

for y in range(y_bound[0], -y_bound[0]):
    y_init = y
    temp_max = 0
    y0 = 0
    step = 0
    x_pos = []
    while y0>y_bound[0]:
        y0 += y
        y -= 1
        step += 1
        if y_bound[0]<=y0<=y_bound[1]:
            if step in pos_steps:
                x_pos.extend(pos_steps[step])
            else:
                x_pos.extend(_list_end_ind)
    count += len(set(x_pos))
print(count)
