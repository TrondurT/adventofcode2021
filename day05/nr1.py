class Line:
    def __init__(self, line:str):
        start, stop = line.split(' -> ')
        self.x1, self.y1 = [int(x) for x in start.split(',')]
        self.x2, self.y2 = [int(x) for x in stop.split(',')]
    def __repr__(self):
        return f'{self.x1},{self.x2} -> {self.x2},{self.y2}'
    def is_hor_or_ver(self):
        return self.x1 == self.x2 or self.y1 == self.y2
    def get_points(self):

        if self.x1 == self.x2:
            ymin = min(self.y1, self.y2)
            ymax = max(self.y1, self.y2)
            return [[y, self.x1] for y in range(ymin, ymax+1)]
            
        elif self.y1 == self.y2:
            xmin = min(self.x1, self.x2)
            xmax = max(self.x1, self.x2)
            return [[self.y1, x] for x in range(xmin, xmax+1)]
        elif abs(self.x2 - self.x1) == abs(self.y2 - self.y1):
            xdiff = self.x2-self.x1
            ydiff = self.y2-self.y1
            xrat = int(xdiff/abs(xdiff))
            yrat = int(ydiff/abs(ydiff))
            return [
                    [y, x] for 
                    x, y in zip(
                        range(
                            self.x1,
                            self.x2+xrat,
                            xrat
                            ),
                        range(
                            self.y1,
                            self.y2+yrat,
                            yrat
                            ),
                        )
                    ]

        raise Exception(self.__repr__())


with open('data.txt', 'r') as f:
    data = [x[:-1] for x in f.readlines()]

lines = [Line(x) for x in data]
hor_lines = [x for x in lines if x.is_hor_or_ver()]

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in lines:
    print(line)
    for i, j in line.get_points():
        grid[i][j] += 1
print(sum([sum([val>1 for val in row]) for row in grid]))
