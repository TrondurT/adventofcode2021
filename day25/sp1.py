with open('data.txt', 'r') as f:
    Data = [x.strip() for x in f]

class Map:
    def __init__(self, data):
        self.height = len(data)
        self.lenght = len(data[0])
        self.grid = []
        self.E = []
        self.S = []
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                if val == '>':
                    self.grid.append((i, j))
                    self.E.append((i, j))
                elif val == 'v':
                    self.grid.append((i, j))
                    self.S.append((i, j))

    def print_map(self):
        print((2+self.lenght)*'-')
        for i in range(self.height):
            _build = ''
            for j in range(self.lenght):
                _next = ' '
                if (i, j) in self.E:
                    _next = '>'
                elif (i, j) in self.S:
                    _next = 'v'
                _build += _next
            print('|'+_build+'|')
        print((2+self.lenght)*'-')

    def move(self):
        b1 = self.move_E()
        b2 = self.move_S()
        return b1 or b2

    def move_E(self):
        move_list = []
        remove_list = []
        for i, j in self.E:
            if j<self.lenght-1:
                J = j+1
            else:
                J = 0
            if (i, J) not in self.grid:
                remove_list.append((i, j))
                move_list.append((i, J))
        for m, rm in zip(move_list, remove_list):
            self.E.remove(rm)
            self.grid.remove(rm)
            self.E.append(m)
            self.grid.append(m)
        return bool(move_list)

    def move_S(self):
        move_list = []
        remove_list = []
        for i, j in self.S:
            if i<self.height-1:
                I = i+1
            else:
                I = 0
            if (I, j) not in self.grid:
                remove_list.append((i, j))
                move_list.append((I, j))
        for m, rm in zip(move_list, remove_list):
            self.S.remove(rm)
            self.grid.remove(rm)
            self.S.append(m)
            self.grid.append(m)
        return bool(move_list)




if __name__ == '__main__':
    import time
    _map = Map(Data)
    i = 0
    while _map.move():
        i+=1
        print(i, time.time())
        #_map.print_map()
    print(i+1)
