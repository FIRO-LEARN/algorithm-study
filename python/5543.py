if __name__ == '__main__':
    sangdukBurger = int(input())
    jungdukBurger = int(input())
    hadukBurger = int(input())
    burgerList = []
    coke = int(input())
    chilsung = int(input())
    tansanDrinkList = []

    burgerList.append(sangdukBurger)
    burgerList.append(jungdukBurger)
    burgerList.append(hadukBurger)

    minValueBurger = burgerList[0]
    for i in range(1, len(burgerList)):
        if minValueBurger > burgerList[i]:
            minValueBurger = burgerList[i]

    tansanDrinkList.append(coke)
    tansanDrinkList.append(chilsung)

    minValueTansan = tansanDrinkList[0]
    for i in range(1, len(tansanDrinkList)):
        if minValueTansan > tansanDrinkList[i]:
            minValueTansan = tansanDrinkList[i]
    print(minValueBurger + minValueTansan - 50)
