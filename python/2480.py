if __name__ == '__main__':
    data = input().split()

    if data[0] == data[1] == data[2]:
        print(10000+int(data[0])*1000)
    elif data[0] == data[1] != data[2]:
        print(1000+int(data[0])*100)
    elif data[0] != data[1] == data[2]:
        print(1000 + int(data[1]) * 100)
    elif data[1] != data[0] == data[2]:
        print(1000 + int(data[0]) * 100)
    else:
        maxValue = data[0]
        for i in range(1, len(data)):
            if maxValue < data[i]:
                maxValue = data[i]
        print(int(maxValue)*100)
