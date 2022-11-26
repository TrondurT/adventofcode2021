with open('data.txt', 'r') as f:
    x, y, aim = 0, 0, 0

    for line in f.read().split('\n'):
        try:
            com, arg = line.split()
        except ValueError:
            break
        if com == 'forward':
            x += int(arg)
            y += aim * int(arg)
        elif com == 'down':
            aim += int(arg)
        elif com == 'up':
            aim -= int(arg)
        else:
            print(com)
print(x, y)
print(x*y)

