if __name__ == '__main__':
    import sys
    index = int(input())
    value = 0

    for i in range(0,index):
        line = int(sys.stdin.readline().rstrip())
        if i != index - 1:
            value = value + (line - 1)
        else:
            value = value + line
    print(value)
