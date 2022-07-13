if __name__ == '__main__':

    v = input().split()

    if v < 1 or v > 6:
        print("score range error")
    else:
        if v >= 90 and v <= 100:
            print("A")
        elif v >= 80 and v <= 89:
            print("B")
        elif v >= 70 and v <= 79:
            print("C")
        elif v >= 60 and v <= 69:
            print("D")
        else:
            print("F")