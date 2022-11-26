class Mace:
    dist = {}
    for i in range(1, 8):
        for j in range(8, 24):
            if i>=j:
                break
            if i<8:
                if j<8:
                    val = j-i -(i==1)-(j==7)
                if j<12:
                    val = 2*int(abs(i-(j-5.5))//1+1)-(i in [1, 7])
                elif j<16:
                    val = 2*int(abs(i-(j-9.5))//1+1)+1-(i in [1, 7])
                elif j<20:
                    val = 2*int(abs(i-(j-13.5))//1+1)+2-(i in [1, 7])
                else:
                    val = 2*int(abs(i-(j-17.5))//1+1)+3-(i in [1, 7])
            else:
                raise Exception
            dist[(i, j)] = val
            dist[(j, i)] = val

    energy_cost = [
               1,    1,   1,     1,
              10,   10,   10,   10, 
             100,  100,  100,  100,
            1000, 1000, 1000, 1000
            ]
    def __init__(self, perm, quick=True):
        self.perm = list(perm)
        self.quick = quick

    def print_perm(self):
        l1 = [x for x in'#############']
        l2 = [x for x in'#           #']
        l3 = [x for x in'### # # # ###']
        l4 = [x for x in'  # # # # #  ']
        l5 = [x for x in'  # # # # #  ']
        l6 = [x for x in'  # # # # #  ']
        l7 = [x for x in'  #########  ']
        for sym, pos in zip('AAAABBBBCCCCDDDD', self.perm):
            if pos<8:
                l2[2*(pos-2)+2+(pos==1)-(pos==7)] = sym
            elif pos<12:
                l3[2*(pos-8)+3] = sym
            elif pos<16:
                l4[2*(pos-12)+3] = sym
            elif pos<20:
                l5[2*(pos-16)+3] = sym
            else:
                l6[2*(pos-20)+3] = sym
        print(''.join(l1))
        print(''.join(l2))
        print(''.join(l3))
        print(''.join(l4))
        print(''.join(l5))
        print(''.join(l6))
        print(''.join(l7))
    
    def find_move(self):
        cand = []
        costes = []
        for i, point in enumerate(self.perm):
            if point<8:
                temp_point = point + 5
                if (point not in [1, 2, 7]) and\
                        (temp_point not in self.perm) and\
                        ((temp_point)%4)==i//4:

                    _insert = True
                    for pos in range(temp_point, 24, 4):
                        if pos in self.perm:
                            room_i = self.perm.index(pos)
                            _insert = _insert and ((room_i//4)==(i//4))
                        else:
                            temp_point = pos
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = temp_point
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, temp_point)] *\
                                        self.energy_cost[i])
                temp_point = point + 6
                if (point not in [1, 6, 7]) and\
                        temp_point not in self.perm and\
                        ((temp_point)%4)==i//4:

                    _insert = True
                    for pos in range(temp_point, 24, 4):
                        if pos in self.perm:
                            room_i = self.perm.index(pos)
                            _insert = _insert and ((room_i//4)==(i//4))
                        else:
                            temp_point = pos
                        pass
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = temp_point
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, temp_point)] *\
                                        self.energy_cost[i])
                for point_ind in range(point-1, 2, -1):
                    if point_ind in self.perm:
                        break
                    temp_point = point_ind+5
                    if temp_point in self.perm or\
                            ((temp_point)%4)!=i//4:
                        continue
                    _insert = True
                    for pos in range(temp_point, 24, 4):
                        if pos in self.perm:
                            room_i = self.perm.index(pos)
                            _insert = _insert and ((room_i//4)==(i//4))
                        else:
                            temp_point = pos
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = temp_point
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, temp_point)] *\
                                        self.energy_cost[i])
                for point_ind in range(point+1, 6):
                    if point_ind in self.perm:
                        break
                    temp_point = point_ind + 6
                    if temp_point in self.perm or\
                            ((temp_point)%4)!=i//4:
                        continue
                    _insert = True
                    for pos in range(temp_point, 24, 4):
                        if pos in self.perm:
                            try:
                                room_i = self.perm.index(pos)
                            except Exception as e:
                                print(temp_point)
                                raise e
                            _insert = _insert and ((room_i//4)==(i//4))
                        else:
                            temp_point = pos
                        pass
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = temp_point
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, temp_point)] *\
                                        self.energy_cost[i])
            else:
                temp_point = point
                # tjekka um hesin er komin uppá pláss
                _cor_column = ((temp_point%4)==(i//4))
                for pos in range(temp_point+4, 24, 4):
                    if self.perm.index(pos)//4 != i//4:
                        _cor_column = False
                        break
                if _cor_column:
                    continue
                # tjekka um hann kann flyta seg
                _continue = False
                for temp_point in range(temp_point-4, 7, -4):
                    if temp_point in self.perm:
                        _continue = True
                        continue
                if _continue:
                    continue
                point_out = temp_point - 6
                # hygg eftir øllum útvegum
                for end in range(point_out, 0, -1):
                    if end in self.perm:
                        break
                    new_move = self.perm.copy()
                    new_move[i] = end
                    cand.append(new_move)
                    costes.append(
                            self.dist[(point, end)] *\
                                    self.energy_cost[i])
                for end in range(point_out+1, 8):
                    if end in self.perm:
                        break
                    new_move = self.perm.copy()
                    new_move[i] = end
                    cand.append(new_move)
                    costes.append(
                            self.dist[(point, end)] *\
                                    self.energy_cost[i])
        return cand, costes

    def __bool__(self):
        _bool = True
        p = self.perm
        if 8 not in p[0:4]:
            return False
        if 12 not in p[0:4]:
            return False
        if 9 not in p[4:8]:
            return False
        if 13 not in p[4:8]:
            return False
        if 10 not in p[8:12]:
            return False
        if 14 not in p[8:12]:
            return False
        if 11 not in p[12:16]:
            return False
        if 15 not in p[12:16]:
            return False
        return True
                    




#start_perm = (
#        15, 18, 20, 23,
#         8, 10, 14, 17,
#         9, 13, 19, 22,
#        11, 12, 16, 21
#        )
#data
start_perm = (
         8, 15, 18, 21,
        10, 14, 17, 23,
         9, 11, 13, 19,
        12, 16, 20, 22
        )
to_check = {start_perm: [0, 0]}
checked = {}

i=0
while to_check:
    m = 999999999999999
    for key in to_check:
        M = to_check[key][0]
        if M<m:
            _perm = key
            m=M
    _price, prev = to_check.pop(_perm)
    checked[_perm] = [_price, prev]
    i+=1
    _mace = Mace(_perm)
    if i%1000==0:
        print(_price)
        _mace.print_perm()
    #input()
    if _mace:
        print(_price)
        break
    cands, costes = _mace.find_move()
    for cand, price in zip(cands, costes):
        for x1, x2, x3, x4 in[
                [ 0,  1,  2,  3],
                [ 4,  5,  6,  7], 
                [ 8,  9, 10, 11], 
                [12, 13, 14, 15]]:
            temp_list = cand[x1:x4+1]
            temp_list.sort()
            cand[x1] = temp_list[0]
            cand[x2] = temp_list[1]
            cand[x3] = temp_list[2]
            cand[x4] = temp_list[3]
        cand = tuple(cand)
        if cand in checked:
            continue
        tot_price = _price + price
        if cand in to_check:
            if tot_price<to_check[cand][0]:
                to_check[cand] = tot_price, _perm
            else:
                continue
        else:
            to_check[cand] = tot_price, _perm
else:
    print('WTF')

input('done')
perms = []
perms.append(checked[_perm])
while perms[-1][1]:
    perms.append(checked[perms[-1][1]])
perms.pop()
perms.reverse()
perms.append([0, _perm])
for perm in perms:
    Mace(perm[1]).print_perm()
    input()
    print(perm[0])

print(_price)
import IPython
IPython.embed()



#start_perm = (
#        15, 18, 20, 23,
#         8, 10, 14, 17,
#         9, 13, 19, 22,
#        11, 12, 16, 21
#        )
#start_perm = (
#         8, 15, 18, 21,
#        10, 14, 17, 23,
#         9, 11, 13, 19,
#        12, 16, 20, 22
#        )
#mace = Mace(start_perm)
#mace.print_perm()
#cands, costes = mace.find_move()
#for cand, price in zip(cands, costes):
#    print('-------------------')
#    mace.print_perm()
#    m = Mace(cand)
#    Mace(cand).print_perm()
#    print(price)
#    input()
