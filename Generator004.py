def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0, *L, 0]
        L = [L1[i] + L1[i + 1] for i in range(len(L1) - 1)]


t = triangles()
print(next(t))
print(next(t))
print(next(t))
print(next(t))
