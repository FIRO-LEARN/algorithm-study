if __name__ == '__main__':
    value = int(input())

    for i in range(value):
        a, b = map(int, input().split())
        print(a + b)
