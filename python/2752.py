if __name__ == '__main__':
    value = input().split()
    value = list(map(int, value))

    value.sort()
    print(*value)
