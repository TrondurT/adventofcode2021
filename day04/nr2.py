class Plate:
    def __init__(self, numbers):
        self.numbers = [[int(x) for x in num.split()] for num in numbers[1:]]
        self.last_number = 0
    def __repr__(self):
        return '\n'.join(['  '.join([f'{y:2}' for y in x]) for x in self.numbers])
    def newnumber(self, number:int):
        '''
        set hettar nummari til 0
        '''
        self.last_number = number
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.numbers[i][j] = 0
    def __bool__(self):
        for i in range(5):
            sum1 = 0
            sum2 = 0
            for j in range(5):
                sum1 += self.numbers[i][j]
                sum2 += self.numbers[j][i]
            if sum1==0 or sum2 == 0:
                return True
        return False
    def score(self):
        return self.last_number * sum((sum(x) for x in self.numbers))


with open('data.txt', 'r') as f:
    data = [x[:-1] for x in f.readlines()]
numbers = data.pop(0)
numbers = [int(x) for x in numbers.split(',')]
plates = [Plate(data[i:i+6]) for i in range(0, len(data), 6)]

for number in numbers:
    for plate in plates:
        plate.newnumber(number)
        if all([bool(_plate) for _plate in plates]):
            print(plate.score())
            exit()
