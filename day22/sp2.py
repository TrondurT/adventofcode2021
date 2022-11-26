with open('data.txt', 'r') as f:
    data = []
    for line in f:
        row = []
        data.append(row)
        sp = line.strip().split()
        row.append(sp[0]=='on')
        for st in sp[1].split(','):
            temp = [int(x) for x in st.split('=')[1].split('..')]
            if temp[1]<temp[0]:
                raise Exception
            row.append(temp)

class State:
    def __init__(self, data):
        self.data = data
        self.set_greinsir()
        self.grid = [
                [
                    [
                        0 for _ in self.z
                    ]
                    for _ in self.y
                ]
                for _ in self.x
            ]

    def set_greinsir(self):
        x = set()
        y = set()
        z = set()
        for row in self.data:
            x.update([row[1][0], row[1][1]+1])
            y.update([row[2][0], row[2][1]+1])
            z.update([row[3][0], row[3][1]+1])
        self.x = list(x)
        self.y = list(y)
        self.z = list(z)
        self.x.sort()
        self.y.sort()
        self.z.sort()

    def get_bound(self, _list, _set):
        return _set.index(_list[0]), _set.index(_list[1]+1)

    def turn_on_off(self):
        for i, row in enumerate(self.data):
            val = 1 if row[0] else 0
            x_b = self.get_bound(row[1], self.x)
            y_b = self.get_bound(row[2], self.y)
            z_b = self.get_bound(row[3], self.z)
            for x in range(x_b[0], x_b[1]):
             for y in range(y_b[0], y_b[1]):
              for z in range(z_b[0], z_b[1]):
                  self.grid[x][y][z] = val

    def count(self):
        count = 0
        for x_m, row in enumerate(self.grid[:-1]):
         for y_m, stack in enumerate(row[:-1]):
          for z_m, val in enumerate(stack[:-1]):
              if val:
                  count += (self.x[x_m+1]-self.x[x_m]) *\
                           (self.y[y_m+1]-self.y[y_m]) *\
                           (self.z[z_m+1]-self.z[z_m])
        return count
        

if __name__ == '__main__':
    state = State(data)
    state.turn_on_off()
    print(state.count())
