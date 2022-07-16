if __name__ == '__main__':
    index = int(input())

    value = ''
    for x in range(index,0,-1):
        for y in range(0, x):
            value = value + '*'
        print(value)
        value = ''
