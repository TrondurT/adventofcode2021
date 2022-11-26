perms = []
perms.append(checked[_perm])
while perms[-1][1]:
    perms.append(checked[perms[-1][1]])
perms.pop()
perms.reverse()
perms.append([0, _perm])
for perm in perms:
    Mace(perm[1]).print_perm()
    input()
    print(perm[0])
