if __name__ == '__main__':
    import sys

    data = []
    while True:
            line = sys.stdin.readline().rstrip()
            if line == '0 0':
                break
            data.append(list(map(int, line.rstrip().split(' '))))

    for i in range(0, len(data)):
        if data[i][0] > data[i][1]:
            print('Yes')
        else:
            print('No')
