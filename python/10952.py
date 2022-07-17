if __name__ == '__main__':
    import sys

    data = []
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '0 0':
            break
        data.append(list(map(int, line.rstrip().split(' '))))
    for x in range(0,len(data)):
        print(data[x][0] + data[x][1])
