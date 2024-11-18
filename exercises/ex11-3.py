def sum_common(list1, list2):
    if len(list1) == 0:
        return 0
    elem = list1.pop(0)
    if elem in list2:
        return sum_common(list1, list2) + elem
    return sum_common(list1, list2) + 0


if __name__ == '__main__':
    print(sum_common([4, 6, 7, 3, 2], [4, 3, 5, 9, 6])) #13
    print(sum_common([1, 5, 4], [2, 3, 6])) #0
    print(sum_common([], [6, 4, 2, 3])) #0
    print(sum_common([1, 2, 3, 4], [4, 3, 2, 1])) #10
