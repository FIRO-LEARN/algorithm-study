if __name__ == '__main__':
    import sys

    data = []
    y=0
    while True:
            line = sys.stdin.readline().rstrip()
            if line == '#':
                break
            data.append(list(map(str, list(line.rstrip().lower()))))

    for i in range(0,len(data)):
        for x in range(0,len(data[i])):
            if (data[i][x] == 'a') or (data[i][x] == 'e') or (data[i][x] == 'i') or (data[i][x] == 'o') or (data[i][x] == 'u'):
                y = y + 1
        print(y)
        y=0
