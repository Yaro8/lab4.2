if __name__ == '__main__':
    class Stack(object):

        def __init__(self, list):
            self.list = [i for i in reversed(list)]

        def append(self, *bonus):
            for elements in bonus:
                self.list.insert(0, elements)

        def copy(self):
            return Stack(list(reversed(self.list)))

        def pop(self):
            return self.list.pop(0)

        def extend(self, stack):
            stack.list += self.list
            self.list = stack.list
            return self.list

        def next(self):
            noviy_spisok = []
            noviy_spisok = self.list.copy()
            noviy_spisok.pop(0)
            return Stack(list(reversed(noviy_spisok)))

        def __str__(self):
            dublb = self.list
            string = ''
            string += '->'.join(str(v) for v in dublb)
            return '[' + string + ']'

        def __add__(self, other):
            new_list = other.list + self.list
            return Stack(list(reversed(new_list)))

        def __iadd__(self, other):
            self.list += other.list
            return Stack(list(reversed(self.list)))

        def __eq__(self, other):
            if self.list == other.list:
                return True
            else:
                return False

        def __rshift__(self, other):
            n = other
            while n > 0:
                self.list.pop(0)
                n -= 1
            return Stack(list(reversed(self.list)))

        def __next__(stack):
            noviy_spisok = []
            noviy_spisok = stack.list.copy()
            noviy_spisok.pop(0)
            return Stack(list(reversed(noviy_spisok)))

    s1 = Stack([1, 2, 3])
    print(s1)
    s1.append(4, 5)
    print(s1)
    s2 = s1.copy()
    sx = s1.copy()
    print(sx.pop())
    print(sx)
    print(s2)
    print(s1 == s2, id(s1) == id(s2))
    s3 = s2.next()
    print(s1, s2, s3, sep='\n')
    print(s1 + s3)
    s3.extend(Stack([1, 2]))
    print(s3)
    s4 = Stack([1, 2])
    s4 += s3 >> 4
    print(s4)
    s5 = next(s4)
    print(s4)
    print(s5)
    s6 = s5.next()
    print(s4, s5, s6, sep='\n')