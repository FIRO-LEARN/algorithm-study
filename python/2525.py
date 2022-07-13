if __name__ == '__main__':
    v = input().split()
    w = int(input())
    h = int(v[0])
    m = int(v[1]) + w

    while m >= 60:
        m = m - 60
        h = h + 1

    if h >= 24:
        h = h - 24

    print(str(h) + ' ' + str(m))
