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

less = list(pos_steps.keys())
less.sort()
some_bool = False
if _list_end_ind:
    cur_min = min((min(pos_steps[x]) for x in _list_end_ind))
    some_bool = all((x in less for x in range(1, cur_min)))

if some_bool:
    y_init = -y_bound[0]-1
    print(int((y_init)*(y_init+1)/2))
else:
    raise Exception
    y_init = 0
    _max = 0
    y_hit = []
    _bool = True
    while True:
        y_init +=1
        y = y_init
        temp_max = 0
        y0 = 0
        for step in range(max(pos_steps.keys())+1):
            y0 += y
            y -= 1
            temp_max = max(temp_max, y0)
            if y_bound[0]<=y0<=y_bound[1]:
                _max = max(_max, temp_max)
                y_hit.append([y_init, y0, step, temp_max])
                print(y_hit[-1])

        if y0>y_bound[1]:
            print(y0, y_init)
            print(step, _max, temp_max)
            break

