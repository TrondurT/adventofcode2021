PAD = 10

with open('data.txt', 'r') as f:
    key = f.readline().strip()
    f.readline()
    temp = []
    for i in f:
        temp.append(i.strip())
    l = len(i.strip())

reverce = (key[0] == '#')

_pad = (2*PAD+l)*[0]
data = []
for _ in range(PAD):
    data.append(_pad)
for row in temp:
    _row = PAD*[0]
    data.append(_row)
    for sym in row:
        _row.append(1 if sym=='#' else 0)
    _row.extend(PAD*[0])
for _ in range(PAD):
    data.append(_pad)

key_dict = {}

i=0
for i1 in [0, 1]:
 key_dict[i1] = {}
 for i2 in [0, 1]:
  key_dict[i1][i2] = {}
  for i3 in [0, 1]:
   key_dict[i1][i2][i3] = {}
   for i4 in [0, 1]:
    key_dict[i1][i2][i3][i4] = {}
    for i5 in [0, 1]:
     key_dict[i1][i2][i3][i4][i5] = {}
     for i6 in [0, 1]:
      key_dict[i1][i2][i3][i4][i5][i6] = {}
      for i7 in [0, 1]:
       key_dict[i1][i2][i3][i4][i5][i6][i7] = {}
       for i8 in [0, 1]:
        key_dict[i1][i2][i3][i4][i5][i6][i7][i8] = {}
        for i9 in [0, 1]:
         temp = 1 if key[i]=='#' else 0
         i += 1
         key_dict[i1][i2][i3][i4][i5][i6][i7][i8][i9] = temp


L = len(data[0])
R = len(data)
temp = key_dict
for row_i in range(3, 6):
    i1, i2, i3 = data[row_i][3:6]
    temp = temp[i1][i2][i3]

def print_im(data):
    print((L+2)*'-')
    for row in data:
        print('|', end='')
        for val in row:
            if val ==1:
                print('#', end='')
                continue
            print(' ', end='')
        print('|')
    print((L+2)*'-')

def get_pix(data, row_mid, ele_mid):
    temp = key_dict
    for row_i in range(row_mid-1, row_mid+2):
        i1, i2, i3 = data[row_i][ele_mid-1:ele_mid+2]
        temp = temp[i1][i2][i3]
    return temp


n = 0
def update_im(data):
    global n
    n+=1
    temp = data
    data = []
    for row_i in range(R):
        _row = []
        data.append(_row)
        for ele_i in range(L):
            #TODO make this right
            if not (0<row_i<R-1 and 0<ele_i<L-1):
                if reverce:
                    _row.append(n%2)
                else:
                    _row.append(0)
                continue
            _row.append(get_pix(temp, row_i, ele_i))
    return data

if __name__ == '__main__':
    #print_im(data)
    data = update_im(data)
    #print_im(data)
    data = update_im(data)
    #print_im(data)
    print(sum((sum(i for i in row)for row in data[1:-1])))
