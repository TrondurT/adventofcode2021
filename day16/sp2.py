table = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

class End_of_mess(Exception):
    pass

class Decode:

    def __init__(self, my_file):
        self.file = open(my_file, 'r')
        self.buff = []
        self.next_bit = self.readbit()

    def readbit(self):
        x = self.file.read(1)
        while x and x!='\n':
            for y in table[x]:
                yield y
            x = self.file.read(1)

    def get_bits(self, count:int, ver=False):
        out = []
        _len = len(self.buff)
        if _len == 0 and ver:
            while True:
                try:
                    next_item = next(self.next_bit)
                except StopIteration:
                    raise End_of_mess
                self.buff.append(next_item)
                if next_item != '0':
                    break
            _len = len(self.buff)

        if _len > count:
            for _ in range(count):
                out.append(self.buff.pop(0))
            count = 0
        else:
            out = self.buff
            self.buff = []
            count -= _len

        for _ in range(count):
            out.append(next(self.next_bit))
        return ''.join(out)

class Operations:
    def __init__(self, _file):
        self.d = Decode(_file)
        self.ops = []
        self.nest = []

    def make_number(self, bits):
        return sum(
                [int(val)*2**i 
                for i, val in enumerate(bits[::-1])
                ])

    def com_4(self):
        _bool = True
        _sum = 0
        bits = ''
        while _bool:
            temp = self.d.get_bits(5)
            _sum += 5
            _bool = (temp[0]=='1')
            bits += temp[1:]

        return [self.make_number(bits), _sum]

    def next_ops(self):
        bits = self.d.get_bits(3, ver=True)
        ver = [self.make_number(bits), len(bits)]
        bits = self.d.get_bits(3)
        com = [self.make_number(bits), len(bits)]

        if com[0] == 4:
            arg = self.com_4()
        else:
            I = self.d.get_bits(1)
            if I == '1':
                arg = [I, self.make_number(self.d.get_bits(11))]
            else:
                arg = [I, self.make_number(self.d.get_bits(15))]
        self.ops.append([ver, com, arg])

    def combine(self):
        self.nest, _ = self._combine(self.ops.copy())

    def _combine(self, _list, term=None, num=0):
        out = []
        use = []
        cum_sum = 0
        _build = []
        _bool = True
        num_hist = []
        while _bool and _list:
            _sum = 0
            nr2_sum = 0
            item = _list.pop(0)
            cum_sum += 6
            nr2_sum += 6
            use.append(item)
            com = item[1][0]
            if com != 4:
                if item[2][0] == '0':
                    if item[2][1] == 0:
                        raise ValueError
                    arg, _sum = self._combine(_list, term='0', num=item[2][1])
                    cum_sum += 16 + _sum
                    nr2_sum += 16 + _sum
                elif item[2][0] == '1':
                    arg, _sum = self._combine(_list, term='1', num=item[2][1])
                    cum_sum += 12 + _sum
                    nr2_sum += 12 + _sum
                else:
                    raise ValueError
            else:#com==4
                arg = item[2][0]
                cum_sum += item[2][1]
                nr2_sum += item[2][1]
            _build.append([com, arg])
            if term == '0':
                num_hist.append((num, nr2_sum))
                num -= nr2_sum
                if num >0:
                    pass
                elif num ==0:
                    _bool = False
                else:
                    raise ValueError
            elif term == '1':
                num -= 1
                if num > 0:
                    pass
                elif num == 0:
                    _bool = False
                else:
                    raise ValueError
            elif term is None:
                pass
            else:
                print(term)
                raise Exception
        return _build, cum_sum

    def exec(self):
        print(self._exec(self.nest[0]))

    def _exec(self, _list):
        if len(_list) == 2:
            if _list[0] == 0:
                ''' sum '''
                _sum = 0
                for item in _list[1]:
                    _sum += self._exec(item)
                return _sum

            elif _list[0] == 1:
                ''' product '''
                _prod = 1
                for item in _list[1]:
                    _prod *= self._exec(item)
                return _prod

            elif _list[0] == 2:
                ''' minimum '''
                _min = None
                for item in _list[1]:
                    cand = self._exec(item)
                    if _min is None:
                        _min = cand
                    else:
                        _min = min(cand, _min)
                return _min

            elif _list[0] == 3:
                ''' maximum '''
                _max = None
                for item in _list[1]:
                    cand = self._exec(item)
                    if _max is None:
                        _max = cand
                    else:
                        _max = max(cand, _max)
                return _max

            elif _list[0] == 4:
                return _list[1]

            elif _list[0] == 5:
                ''' greater than '''
                _bool = (self._exec(_list[1][0]) > self._exec(_list[1][1]))
                if _bool:
                    return 1
                return 0

            elif _list[0] == 6:
                ''' less than '''
                _bool = (self._exec(_list[1][0]) < self._exec(_list[1][1]))
                if _bool:
                    return 1
                return 0

            elif _list[0] == 7:
                ''' equal to '''
                _bool = (self._exec(_list[1][0]) == self._exec(_list[1][1]))
                if _bool:
                    return 1
                return 0

            raise Exception
        else:
            print(len(_list))
            raise Exception
            
        

if __name__ == '__main__':
    o = Operations('data.txt')
    while True:
        try:
            o.next_ops()
        except End_of_mess:
            break
    print(sum([x[0][0] for x in o.ops]))
    o.combine()
    o.exec()
