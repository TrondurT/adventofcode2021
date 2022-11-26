from copy import deepcopy

class Number:
    def __init__(self, num):
        self.num = deepcopy(num)
        self.reduce()

    def __str__(self):
        return str(self.num)

    def explode(self):
        prev = None
        i = [-1]
        _explote = None
        while True:
            if i[-1] < 1:
                i[-1] += 1
            else:
                try:
                    while i[-1] >= 1:
                        i.pop()
                except IndexError:
                    break
                i[-1] += 1
            val = self.num
            for j in i:
                val_list = val
                val = val[j]
            if type(val) == list:
                if len(i) == 4 and not _explote:
                    _explote = val
                    val_list[i[-1]] = 0
                    if prev is not None and prev != 'Done':
                        prev[0][prev[1]] += _explote[0]
                        prev = 'Done'
                else:
                    i.append(-1)
            else:
                if _explote:
                    val_list[i[-1]] +=_explote[1]
                    return True
                if prev != 'Done':
                    prev = [val_list, i[-1]]
        if _explote:
            return True
        return False

    def split(self):
        prev = None
        i = [-1]
        _explote = None
        while True:
            if i[-1] < 1:
                i[-1] += 1
            else:
                try:
                    while i[-1] >= 1:
                        i.pop()
                except IndexError:
                    break
                i[-1] += 1
            val = self.num
            for j in i:
                val_list = val
                val = val[j]
            if type(val) == list:
                i.append(-1)
            else:
                if val>=10:
                    a = val//2
                    b=val-a
                    val_list[i[-1]] = [a, b]
                    return True
                    exit()

    def reduce(self):
        _bool = True
        while _bool:
            _bool = False
            while self.explode():
                _bool=True
            if self.split():
                _bool=True

    def __add__(self, other):
        return Number([deepcopy(self.num), deepcopy(other.num)])

    def mag(self):
        return self._mag(self.num)

    def _mag(self, num):
        if type(num) == int:
            return num
        elif type(num) == list:
            return 3*self._mag(num[0]) + 2*self._mag(num[1])
        else:
            raise Exception


if __name__ == '__main__':
    num = Number([[9, 1], [1, 9]])
    print(num.mag())
