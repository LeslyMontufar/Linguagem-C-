while True:
    try:
        M = float(input())
        L = [float(x) for x in input().split()]
        L.sort()
        Res = max(L)
        while not((Res%L[0]==0) and (Res%L[1]==0)):
            Res += max(L)
        print('{:.0f}'.format(Res - M))
    except EOFError:
        break
