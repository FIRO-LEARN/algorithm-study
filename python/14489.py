if __name__ == '__main__':
    zango = input().split()
    zango = list(map(int, zango))
    chicken = int(input())

    if zango[0] + zango[1] < chicken * 2:
        print(zango[0] + zango[1])
    else:
        print((zango[0] + zango[1]) - chicken * 2)
