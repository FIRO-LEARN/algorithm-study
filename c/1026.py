if __name__ == '__main__':
    index = input()
    value = 0
    notSortList = input().split()
    notSortList = list(map(int, notSortList))
    list1 = input().split()
    list1 = list(map(int, list1))
    list1.sort()

    for i in range(0, len(list1)):
        maxValueInList = list1[0]
        maxValueInListIndex = 0
        for x in range(1, len(notSortList)):
            if maxValueInList < notSortList[x]:
                maxValueInList = notSortList[x]
                maxValueInListIndex = x
        value = value + list1[i] * notSortList[maxValueInListIndex]
        del notSortList[maxValueInListIndex]
    print(value)

