if __name__ == '__main__':
    value = input().split()
    value2 = input().split()
    value3 = ''

    calc1 = int(value[0]) * int(value[1])

    for i in range(0,len(value2)):
        value3 = value3 + str(-(calc1-int(value2[i]))) + ' '
    print(value3)
