if __name__ == '__main__':
    man = int(input())
    man2 = int(input())
    man3 = int(input())
    man4 = int(input())
    man5 = int(input())

    man = 40 if man < 40 else man
    man2 = 40 if man2 < 40 else man2
    man3 = 40 if man3 < 40 else man3
    man4 = 40 if man4 < 40 else man4
    man5 = 40 if man5 < 40 else man5

    print(int((man+man2+man3+man4+man5)/5))
