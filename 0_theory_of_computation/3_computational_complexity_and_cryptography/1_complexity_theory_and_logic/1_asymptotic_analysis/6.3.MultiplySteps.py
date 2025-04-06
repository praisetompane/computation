def multiplyWork(n):
    for i in range(1, n):
        for j in range(1, n):
            print(str(i) + "*" + str(j) + "=" + str(i * j))


multiplyWork(5)
