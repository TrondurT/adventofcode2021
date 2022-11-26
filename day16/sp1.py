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

    def make_number(self, bits):
        return sum(
                [int(val)*2**i 
                for i, val in enumerate(bits[::-1])
                ])

    def com_4(self):
        _bool = True
        bits = ''
        while _bool:
            temp = self.d.get_bits(5)
            _bool = (temp[0]=='1')
            bits += temp[1:]

        return self.make_number(bits)

    def next_ops(self):
        bits = self.d.get_bits(3, ver=True)
        ver = [self.make_number(bits), len(bits)]
        com = self.make_number(self.d.get_bits(3))

        if com == 4:
            arg = self.com_4()
        else:
            I = self.d.get_bits(1)
            if I == '1':
                arg = [I, self.make_number(self.d.get_bits(11))]
            else:
                arg = [I, self.make_number(self.d.get_bits(15))]
        print(ver, com, arg)
        self.ops.append([ver, com, arg])
        

if __name__ == '__main__':
    o = Operations('data.txt')
    while True:
        try:
            o.next_ops()
        except End_of_mess:
            print('end')
            break
    print(sum([x[0][0] for x in o.ops]))

