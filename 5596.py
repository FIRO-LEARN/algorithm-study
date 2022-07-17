if __name__ == '__main__':
    minkuk = input().split()
    mansae = input().split()
    minkuk = list(map(int, minkuk))
    mansae = list(map(int, mansae))

    allMinkuk = int(minkuk[0] + minkuk[1] + minkuk[2] + minkuk[3])
    allMansae = int(mansae[0] + mansae[1] + mansae[2] + mansae[3])

    if allMansae > allMinkuk:
        print(allMansae)
    elif allMinkuk > allMansae:
        print(allMinkuk)
    else:
        print(allMinkuk)
