if __name__ == '__main__':
    index = int(input())

    value = ''
    for x in range(1, index+1):
        for i in range(0, index-x):
            value = value + ' '
        for y in range(0, x):
            value = value + '*'
        print(value)
        value = ''
