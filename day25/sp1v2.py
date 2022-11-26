import time
with open('data.txt', 'r') as f:
    Data = [x.strip() for x in f]

class Map:
    def __init__(self, data):
        self.height = len(data)
        self.lenght = len(data[0])
        self.grid = []
        for i, row in enumerate(data):
            _row = []
            self.grid.append(_row)
            for val in row:
                _row.append(val)

    def print_map(self):
        print((2+self.lenght)*'-')
        for row in self.grid:
            print('|', end='')
            print(''.join(row).replace('.', ' '), end='')
            print('|')
        print((2+self.lenght)*'-')

    def move(self):
        b1 = self.move_E()
        b2 = self.move_S()
        return b1 or b2

    def move_E(self):
        _bool = False
        for i in range(self.height):
            for j in range(self.lenght-1, -1, -1):
                val = self.grid[i][j]
                if val == '>' and self.grid[i][(j+1)%self.lenght]=='.':
                    _bool = True
                    self.grid[i][(j+1)%self.lenght]='E'
                    self.grid[i][j]='+'
        for i in range(self.height):
            for j in range(self.lenght):
                if self.grid[i][j] == '+':
                    self.grid[i][j] = '.'
                if self.grid[i][j] == 'E':
                    self.grid[i][j] = '>'
        return _bool

    def move_S(self):
        _bool = False
        for i in range(self.height-1, -1, -1):
            for j in range(self.lenght):
                val = self.grid[i][j]
                if val == 'v' and self.grid[(i+1)%self.height][j]=='.':
                    _bool = True
                    self.grid[(i+1)%self.height][j]='S'
                    self.grid[i][j]='+'
        for i in range(self.height):
            for j in range(self.lenght):
                if self.grid[i][j] == '+':
                    self.grid[i][j] = '.'
                if self.grid[i][j] == 'S':
                    self.grid[i][j] = 'v'
        return _bool



if __name__ == '__main__':
    tic = time.time()
    _map = Map(Data)
    _map.print_map()
    i = 0
    while _map.move():
        i+=1
        print(i, time.time()-tic)
        _map.print_map()
        time.sleep(2)
    print(i+1)
