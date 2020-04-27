def check_sub(array, k):
    sub_result = set()
    for num in array:
        if num in sub_result:
            return True
        sub_result.add(k - num)

    return False


def check_sub1(array, k):
    for num1 in array:
        array.remove(num1)
        for num2 in array:
            if num1 + num2 == k:
                return True
    return False


assert not check_sub([], 17)
assert check_sub([10, 15, 3, 7], 17)
assert not check_sub([10, 15, 3, 4], 17)
