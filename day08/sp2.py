from pprint import pprint

class Decode_signal:
    def __init__(self, signal:str):

        _sp = signal.split('|')
        self.all_dig = _sp[0].split()
        self.data = _sp[1].split()
        self.make_key()
        

    def make_key(self):

        self.key = {i:'' for i in range(10)}

        for key in self.all_dig:
            _len = len(key)
            if _len == 2:
                self.key[1] = key
            elif _len == 3:
                self.key[7] = key
            elif _len == 4:
                self.key[4] = key
            elif _len == 7:
                self.key[8] = key

        fore_minus_one = self.key[4]
        for car in self.key[1]:
            fore_minus_one = fore_minus_one.replace(car, '')

        for key in self.all_dig:
            _len = len(key)
            if _len == 5:
                if all([x in key for x in self.key[1]]):
                    self.key[3] = key
                elif all([x in key for x in fore_minus_one]):
                    self.key[5] = key
                else:
                    self.key[2] = key
            elif _len == 6:
                if not all([x in key for x in self.key[1]]):
                    self.key[6] = key
                elif all([x in key for x in self.key[4]]):
                    self.key[9] = key
                else:
                    self.key[0] = key
    def make_number(self):
        build = []
        for dig in self.data:
            _len = len(dig)
            if _len == 2:
                build.append('1')
            elif _len == 3:
                build.append('7')
            elif _len == 4:
                build.append('4')
            elif _len == 5:
                _set = set(dig)
                if _set == set(self.key[2]):
                    build.append('2')
                if _set == set(self.key[3]):
                    build.append('3')
                if _set == set(self.key[5]):
                    build.append('5')
            elif _len == 6:
                _set = set(dig)
                if _set == set(self.key[0]):
                    build.append('0')
                if _set == set(self.key[6]):
                    build.append('6')
                if _set == set(self.key[9]):
                    build.append('9')
            elif _len == 7:
                build.append('8')
        return int(''.join(build))


with open('data.txt', 'r') as f:
    Data = [x[:-1] for x in f.readlines()]

cum_sum = 0
for data in Data:
    cum_sum += Decode_signal(data).make_number()
print(cum_sum)
