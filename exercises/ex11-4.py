def deep_add(collection):
    if isinstance(collection, int):
        return collection + 1
    elif collection == []:
        return []
    else:
        return [deep_add(collection[0])] + deep_add(collection[1:])


if __name__ == '__main__':
    print(deep_add([[3, -4, [15]], 0, [[[1]], 61]]))
    #[[4, -3, [16]], 1, [[[2]], 62]]

    print(deep_add([1, [2, 3], [], [4, 5, [6]], 1]))
    #[2, [3, 4], [], [5, 6, [7]], 2]

    print(deep_add([[[[7]]]]))
    #[[[[8]]]]
