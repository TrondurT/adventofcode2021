with open('data.txt', 'r') as f:
    x, y = 0, 0

    for line in f.read().split('\n'):
        try:
            com, arg = line.split()
        except ValueError:
            break
        if com == 'forward':
            x += int(arg)
        elif com == 'down':
            y += int(arg)
        elif com == 'up':
            y -= int(arg)
        else:
            print(com)
print(x, y)
print(x*y)

