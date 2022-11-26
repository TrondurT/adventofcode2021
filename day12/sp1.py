with open('data.txt', 'r') as f:
    temp = [x[:-1] for x in f.readlines()]
    _edge = []
    vertices = set()
    for i in temp:
        x1, x2 = i.split('-')
        _edge.append([x1, x2])
        vertices.add(x1)
        vertices.add(x2)
    edge = {x:[] for x in vertices}
    for x1, x2 in _edge:
        edge[x1].append(x2)
        edge[x2].append(x1)


paths = [['start']]
finish_paths = []

while paths:
    cur_path = paths.pop()
    for ver in edge[cur_path[-1]]:
        my_copy = cur_path.copy()
        if ver == 'end':
            my_copy.append(ver)
            finish_paths.append(my_copy)
            continue
        if ver == 'start':
            continue
        if ver == ver.lower() and ver in cur_path:
            continue
        my_copy.append(ver)
        paths.append(my_copy)
print(len(finish_paths))


