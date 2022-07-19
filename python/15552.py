if __name__ == '__main__':
    import sys
    value = int(input())

    for i in range(value):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a + b)
