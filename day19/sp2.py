with open('data.txt', 'r') as f:
    x = f.readline().strip()
    Data = {}
    while x:
        lable = int(x.strip('-').strip().split()[1])
        Data[lable] = []
        x = f.readline().strip()
        while x:
            Data[lable].append([int(y) for y in x.split(',')])
            x = f.readline().strip()
        x = f.readline().strip()

def make_mat(points):
    mat = []
    for p1 in points:
        row = []
        mat.append(row)
        for p2 in points:
            s = sum((abs(v-w) for v, w in zip(p1, p2)))
            row.append(s)
    return mat

def perm_from_mats(mat1, mat2):
    I, J = len(mat1), len(mat2)
    perm = []

    for i in range(I):
        m = 0
        for j in range(J):
            s = sum((1 for item in mat2[j] if item in mat1[i]))
            if s>m:
                m=s
                p=[j]
            elif m==s:
                p.append(j)
        perm.append([i, p, m])

    _dict = {}
    for row in perm:
        _x = row[2]
        if _x not in _dict.keys():
            _dict[_x] = 0
        _dict[_x] += 1

    match_guess = list(set([x[2] for x in perm]))
    match_guess.sort() 
    match_guess.reverse() 

    for M in match_guess:
        if M == len([p for p in perm if p[2]>=M]):
            break
        elif M <= len([p for p in perm if p[2]>=M]):
            break

    perm = [row for row in perm if row[2]>=M]
    if len(perm)<2:
        raise Exception
    return perm, M

def _find_rot_sign_off(a1, a2, d1, d2, p11, p12, p21, p22):
    sign, rot = [], []
    for i, test in enumerate(a1):
        for j, cand in enumerate(a2):
            if j in rot:
                continue
            if test == cand:
                rot.append(j)
                if d1[i] == d2[j]:
                    sign.append(1)
                else:
                    sign.append(int(d1[i]/d2[j]))
                break
        else:
            return [0, 1, 2], [1, 1, 1], 3*[9999999999999]
    off = []
    off = [x - s*p21[r] for x, s, r in zip(p11, sign, rot)]
    return rot, sign, off

def test_rot(points1, points2, perm, rot, sign, off):
    bools = []

    for per in perm:
        sub_bool = []
        for sub_per in per[1]:
            poi1 = points1[per[0]]
            x = points2[sub_per]
            poi2 = [s*x[r]+o 
                    for s, r, o in zip(sign, rot, off)]
            sub_bool.append(poi1==poi2)
        bools.append(sub_bool)
    return sum([any(x) for x in bools]), bools

    

def find_rot(points1, points2, perm, M):
    combo_dict = {}
    for i, perm1 in enumerate(perm):
        p11 = points1[perm1[0]]
        for perm12 in perm1[1]:
            p21 = points2[perm12]
            for j, perm2 in enumerate(perm):
                if j<=i:
                    continue
                p12 = points1[perm2[0]]
                for perm22 in perm2[1]:
                    if perm22 == perm12:
                        continue
                    p22 = points2[perm22]

                    d1 = [x-y for x, y in zip(p11, p12)]
                    a1 = [abs(x) for x in d1]

                    d2 = [x-y for x, y in zip(p21, p22)]
                    a2 = [abs(x) for x in d2]
                    rot, sign, off = 0, 0, 0

                    _continue = False
                    for t in a1:
                        if t not in a2:
                            continue

                    if len(set(a1)) == 3:
                        rot, sign, off =  _find_rot_sign_off(
                                a1, a2, d1, d2, p11, p12, p21, p22)
                        bool_sum, _bools = test_rot(
                                points1, points2, perm, rot, sign, off
                                )
                    else:
                        bool_sum = -1
                        for _perm in [
                                        [0, 1, 2],
                                        [0, 2, 1],
                                        [1, 0, 2],
                                        [1, 2, 0],
                                        [2, 0, 1],
                                        [2, 1, 0]
                                        ]:
                            _co = False
                            for _i, _el in enumerate(_perm):
                                if a1[_i] != a1[_el]:
                                    _co=True
                                    break
                            if _co:
                                continue

                            rot_temp, sign_temp, off_temp =  _find_rot_sign_off(
                                    [a1[_i] for _i in _perm], 
                                    [a2[_i] for _i in _perm],
                                    [d1[_i] for _i in _perm],
                                    [d2[_i] for _i in _perm],
                                    [p11[_i] for _i in _perm],
                                    [p12[_i] for _i in _perm],
                                    [p21[_i] for _i in _perm],
                                    [p22[_i] for _i in _perm]
                                    )
                            _perm_i = [
                                    [_i, _el] 
                                    for _i, _el in enumerate(_perm)
                                    ]
                            _perm_i.sort(key=lambda x: x[1])
                            _perm_i = [x[0] for x in _perm_i]

                            rot_temp  = [rot_temp[_i] for _i in _perm_i]
                            sign_temp = [sign_temp[_i] for _i in _perm_i]
                            off_temp  = [off_temp[_i] for _i in _perm_i]
                            bool_sum_temp, _bools_temp = test_rot(
                                    points1, points2, perm, 
                                    rot_temp, sign_temp, off_temp
                                    )
                            if bool_sum < bool_sum_temp:
                                bool_sum = bool_sum_temp
                                _bools = _bools_temp
                                rot = rot_temp
                                sign = sign_temp
                                off = off_temp
                    combo_dict[(i, j, perm12, perm22)] = [
                            bool_sum,
                            (rot, sign, off)
                            ]

    N = max((x[0] for x in combo_dict.values()))
    if N<3:
        return (N, N, N), False
    _dict = {}

    for n, val in combo_dict.values():
        if n != N:
            continue
        val = tuple(tuple(x) for x in val)
        if val not in _dict:
            _dict[val] = 0
        _dict[val] += 1

    if len(combo_dict) == _dict[val] or len(_dict)==1:
        return val, True
    else:
        raise Exception


def append_points_list(points, points_new, perm, rot, sign, off):
    for p in points_new:
        points.append([s*p[r]+o for s, r, o in zip(sign, rot, off)])
    points = set(tuple(tuple(x) for x in points))
    points = [list(x) for x in points]
    return points

def get_sol(points1, points2, mat1, mat2):
    perm, M = perm_from_mats(mat1, mat2)
    points = [x.copy() for x in points2]
    (rot, sign, off), _bool = find_rot(points1, points, perm, M)
    return points, rot, sign, off, perm, _bool

mats = {key:make_mat(Data[key]) for key in Data}

my_list = list(Data.keys())[1:]
mydata = [[Data[key], mats[key], key] for key in Data.keys()]
off_list = []

while len(mydata)>1:

    points1, mat1, key1 = mydata.pop(0)
    poplist = [x.copy() for x in mydata]
    switch = False
    for points2, mat2, key2 in poplist:
        if key1>key2:
            key1, key2 = key2, key1
            points1, points2 = points2, points1
            mat1, mat2 = mat2, mat1
            switch = True

        points, rot, sign, off, perm, _bool = get_sol(
                points1, points2, mat1, mat2)
        if not _bool:
            if switch:
                key1 = key2
                points1 = points2
                mat1 = mat2
            continue

        points1 = append_points_list(points1, points2, perm, rot, sign, off)
        mat1 = make_mat(points1)
        if switch:
            for i, x in enumerate(mydata):
                if x[2]==key1:
                    break
            mydata.pop(i)
            off_list.append([key1, key2, off, rot, sign])
        else:
            for i, x in enumerate(mydata):
                if x[2]==key2:
                    break
            mydata.pop(i)
            off_list.append([key1, key2, off, rot, sign])
    mydata.append([points1, mat1, key1])

off_copy = [[x[0], x[1], list(x[2]), list(x[3]), list(x[4])] 
        for x in off_list]
super_list_off = []
super_list_rot = []
super_list_sign = []
end_points = []
i = 0
while i<len(off_copy):
    if off_copy[i][0] == 0:
        temp = off_copy.pop(i)
        super_list_off.append(temp[2])
        super_list_rot.append(temp[3])
        super_list_sign.append(temp[4])
        end_points.append(temp[1])
    else:
        i += 1

i = 0
while i<len(off_copy):
    for j, val in enumerate(end_points):
        if val == off_copy[i][0]:
            break
    else:
        i += 1
        raise Exception
        continue
    temp = off_copy.pop(i)
    p = temp[2]
    pos = [s*p[r]+o for s, r, o in zip(
        super_list_sign[j],
        super_list_rot[j],
        super_list_off[j]
        )]
    super_list_off.append(pos)
    end_points.append(temp[1])

print(max( j for i in make_mat(super_list_off) for j in i))
