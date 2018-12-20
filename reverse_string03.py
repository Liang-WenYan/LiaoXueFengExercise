'''
def zip(a, b):
    return a + b


c = (1, 2)
print(zip(*c))

l = [1, 2]
l.insert(0, 3)
print(l)
'''


class Foo:
    def __str__(self):
        return "I love Yanyan."


def string_reverse2(string):
    t = list(string)
    l = len(t)
    print("l = {}".format(l))
    print(range(l - 1, 0, -1))
    print(list(range(l - 1, 0, -1)))
    print(range(l // 2))
    print(list(range(l // 2)))
    print(zip(range(l - 1, 0, -1), range(l // 2)))
    print(tuple(zip(range(l - 1, 0, -1), range(l // 2))))
    print(list(zip(range(l - 1, 0, -1), range(l // 2))))
    print(dict(zip(range(l - 1, 0, -1), range(l // 2))))
    for i in zip(range(l - 1, 0, -1), range(l // 2)):
        print(i)
        x, y = i
        print(x,y)


    for i,j in zip(range(l - 1, 0, -1), range(l // 2)):
        print(i,j)
        # rint(i, j)
        # t[i], t[j] = t[j], t[i]
    return "".join(t)


print(string_reverse2("I love yanyan."))
