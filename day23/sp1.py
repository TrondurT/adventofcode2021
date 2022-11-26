class Mace:
    dist = {}
    for i in range(1, 8):
        for j in range(8, 16):
            if i>=j:
                break
            if i<8:
                if j<8:
                    val = j-i -(i==1)-(j==7)
                if j<12:
                    val = 2*int(abs(i-(j-5.5))//1+1)-(i in [1, 7])
                else:
                    val = 2*int(abs(i-(j-9.5))//1+1)+1-(i in [1, 7])
            else:
                raise Exception
            dist[(i, j)] = val
            dist[(j, i)] = val

    energy_cost = [1, 1, 10, 10, 100, 100, 1000, 1000]
    def __init__(self, perm, quick=True):
        self.perm = list(perm)
        self.quick = quick

    def print_perm(self):
        l1 = [x for x in'#############']
        l2 = [x for x in'#           #']
        l3 = [x for x in'### # # # ###']
        l4 = [x for x in'  # # # # #  ']
        l5 = [x for x in'  #########  ']
        for sym, pos in zip('AABBCCDD', self.perm):
            if pos<8:
                l2[2*(pos-2)+2+(pos==1)-(pos==7)] = sym
            elif pos<12:
                l3[2*(pos-8)+3] = sym
            else:
                l4[2*(pos-12)+3] = sym
        print(''.join(l1))
        print(''.join(l2))
        print(''.join(l3))
        print(''.join(l4))
        print(''.join(l5))
    
    def find_move(self):
        cand = []
        costes = []
        for i, point in enumerate(self.perm):
            if point<8:
                if (point not in [1, 2, 7]) and\
                        (point+5 not in self.perm) and\
                        ((point+5)-8)==i//2:
                    if point+9 in self.perm:
                        end = point+5
                        room_i = self.perm.index(point+9)
                        _insert = (room_i//2==i//2)
                    else:
                        end = point+9
                        _insert = True
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = end
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, end)] *\
                                        self.energy_cost[i])
                if (point not in [1, 6, 7]) and\
                        point+6 not in self.perm and\
                        ((point+6)-8)==i//2:
                    if point+10 in self.perm:
                        end = point+6
                        room_i = self.perm.index(point+10)
                        _insert = (room_i//2==i//2)
                    else:
                        end = point+10
                        _insert = True
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = end
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, end)] *\
                                        self.energy_cost[i])
                for point_ind in range(point-1, 2, -1):
                    if point_ind in self.perm:
                        break
                    if point_ind+5 in self.perm or\
                            ((point_ind+5)-8)!=i//2:
                        continue
                    end = point_ind+5
                    if point_ind+9 not in self.perm:
                        end = point_ind+9
                        _insert = True
                    else:
                        room_i = self.perm.index(point_ind+9)
                        _insert = (room_i//2==i//2)
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = end
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, end)] *\
                                        self.energy_cost[i])
                for point_ind in range(point+1, 6):
                    if point_ind in self.perm:
                        break
                    if point_ind+6 in self.perm or\
                            ((point_ind+6)-8)!=i//2:
                        continue
                    end = point_ind+6
                    if point_ind+10 not in self.perm:
                        end = point_ind+10
                        _insert = True
                    else:
                        room_i = self.perm.index(point_ind+10)
                        _insert = (room_i//2==i//2)
                    if _insert:
                        new_move = self.perm.copy()
                        new_move[i] = end
                        cand.append(new_move)
                        costes.append(
                                self.dist[(point, end)] *\
                                        self.energy_cost[i])
            else:
                temp_point = point
                if temp_point>11:
                    if (temp_point-12)==(i//2) and self.quick:
                        continue
                    temp_point -= 4
                    if temp_point in self.perm:
                        continue
                else:
                    if (temp_point-8)==(i//2) and self.quick:
                        down_index = self.perm.index(temp_point+4)
                        if down_index//2 == i//2:
                            continue
                point_out = temp_point - 6
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
        if 8 not in p[0:2]:
            return False
        if 12 not in p[0:2]:
            return False
        if 9 not in p[2:4]:
            return False
        if 13 not in p[2:4]:
            return False
        if 10 not in p[4:6]:
            return False
        if 14 not in p[4:6]:
            return False
        if 11 not in p[5:]:
            return False
        if 15 not in p[5:]:
            return False
        return True
                    




#example
#start_perm = (12, 15, 8, 10, 9, 14, 11, 13)
#Data
start_perm = (8, 13, 10, 15, 9, 11, 12, 14)
to_check = {start_perm: [0, 0]}
checked = {}

while to_check:
    m = 999999999999999
    for key in to_check:
        M = to_check[key][0]
        if M<m:
            _perm = key
            m=M
    _price, prev = to_check.pop(_perm)
    checked[_perm] = [_price, prev]
    _mace = Mace(_perm)
    #print(_price)
    #_mace.print_perm()
    #input()
    if _mace:
        print(_price)
        break
    cands, costes = _mace.find_move()
    for cand, price in zip(cands, costes):
        for x1, x2 in[[0, 1], [2, 3], [4, 5], [6, 7]]:
            m = min(cand[x1:x2+1])
            M = max(cand[x1:x2+1])
            cand[x1] = m
            cand[x2] = M
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

#import IPython
#IPython.embed()



#start_perm = (12, 15, 8, 10, 9, 14, 11, 13)
#start_perm = (8, 13, 10, 15, 9, 11, 12, 14)
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
