with open('data.txt', 'r') as f:
    data = {}
    for i, d in enumerate(f):
        # teir eru á felt eitt minni enn teir eru á
        data[i] = int(d.split(':')[1].strip())-1

dice = {
        3 : 1,
        4 : 3,
        5 : 6,
        6 : 7,
        7 : 6,
        8 : 3,
        9 : 1
        }

count = [0, 0]
def count_win(state, sc, pl, rep, dep):

    for key in dice:
        data = state.copy()
        _sc = sc.copy()
        _rep = rep * dice[key]

        data[pl] = (data[pl] + key) % 10
        _sc[pl] = _sc[pl] + data[pl] + 1
        if _sc[pl] >= 21:
            count[pl] += _rep
            continue
        count_win(state=data, sc=_sc, pl=(pl+1)%2, rep=_rep, dep=dep+1)

    

if __name__ == '__main__':
    count_win(data, {0:0, 1:0}, 0, rep=1, dep=0)
    print(max(count))
