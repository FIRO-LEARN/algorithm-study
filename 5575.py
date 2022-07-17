if __name__ == '__main__':
    a = input().split()
    b = input().split()
    c = input().split()

    aH = int(a[3]) - int(a[0])
    aM = int(a[4]) - int(a[1])
    aS = int(a[5]) - int(a[2])

    if aS < 0:
        aM = aM - 1
        aS = aS + 60
    if aM < 0:
        aH = aH - 1
        aM = aM + 60
    print(aH,aM,aS)

    bH = int(b[3]) - int(b[0])
    bM = int(b[4]) - int(b[1])
    bS = int(b[5]) - int(b[2])

    if bS < 0:
        bM = bM - 1
        bS = bS + 60
    if bM < 0:
        bH = bH - 1
        bM = bM + 60
    print(bH,bM,bS)

    cH = int(c[3]) - int(c[0])
    cM = int(c[4]) - int(c[1])
    cS = int(c[5]) - int(c[2])

    if cS < 0:
        cM = cM - 1
        cS = cS + 60
    if cM < 0:
        cH = cH - 1
        cM = cM + 60
    print(cH,cM,cS)
