with open('work_neq_5_6.txt', 'r') as f:
    Data = [x.strip() for x in f]

class ALU:
    def __init__(self, data):
        self.data = data
        self.w  = ''
        self.x  = ''
        self.y  = ''
        self.z  = ''
        self._divlist = []

    def decode(self):
        var = (f'i_{i}' for i in range(1, 100))
        print()
        for i, row in enumerate(self.data):
            ins = row.split()
            if row == 'exit':
                exit()
            op = ins[0]

            if op == 'inp':
                arg1 = ins[1]
                self.__dict__[ins[1]] = f'({next(var)})'

            elif op =='mul':
                arg1, arg2 = self.get_args(ins[1:])
                if arg1 =='':
                    pass
                elif arg2 == 0:
                    self.__dict__[ins[1]] = ''
                elif arg2 == 1 or arg2 == '1':
                    pass
                else:
                    self.__dict__[ins[1]] = f'({arg1}*{arg2})'

            elif op == 'add':
                arg1, arg2 = self.get_args(ins[1:])
                if arg1 =='':
                    self.__dict__[ins[1]] = arg2
                elif arg2 == 0 or arg2 == '':
                    pass
                else:
                    self.__dict__[ins[1]] = f'({arg1}+{arg2})'

            elif op == 'mod':
                arg1, arg2 = self.get_args(ins[1:])

                if type(arg2)==int:
                    if arg2<1:
                        raise Exception
                else:
                    print(arg2)
                    print('fixme')
                    print()
                    raise Exception

                if arg1 == '':
                    pass
                #eg fangi tað longur uppi um hetta ikki burda rigga
                elif type(arg2)==int:
                    self.__dict__[ins[1]] = f'({arg1}%{arg2})'

                else:
                    raise Exception

            elif op == 'div':
                arg1, arg2 = self.get_args(ins[1:])

                if type(arg2)==int:
                    if arg2==0:
                        raise Exception
                else:
                    print(arg2)
                    print('fixme')
                    print()
                    raise Exception

                if arg2 == 1:
                    pass
                else:
                    self.__dict__[ins[1]] = f'({arg1}//{arg2})'

            elif op == 'eql':
                arg1, arg2 = self.get_args(ins[1:])
                arg1 = arg1 or 0
                arg2 = arg2 or 0
                self.__dict__[ins[1]] = (op, arg1, arg2)
                self.__dict__[ins[1]] = f'({arg1}=={arg2})'
                
            else:
                print('---')
                print(row)
                print('---')
                exit()

            print(i, row)
            print(f'w={self.w}\nx={self.x}\ny={self.y}\nz={self.z}')
            modify = ''
            #modify = input()
            #print(f'w={self.w}')
            while modify:
                try:
                    args = [x.strip() for x in modify.split('=')]
                    self.__dict__[args[0]] = args[1]
                    print()
                except:
                    pass
                print(f'w={self.w}\nx={self.x}\ny={self.y}\nz={self.z}\n')
                modify = input()

    def get_args(self, _list):
        arg1 = self.__dict__[_list[0]]
        if len(_list)==1:
            arg2 = None
        else:
            try:
                arg2 = int(_list[1])
            except ValueError:
                arg2 = self.__dict__[_list[1]]
            except Exception as e:
                raise e
        return arg1, arg2


if __name__ == '__main__':
    alu = ALU(Data)
    alu.decode()
