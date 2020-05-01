def remove_neg_and_arrange(array):
    positive_array = []
    for num in array:
        if num > 0:
            positive_array.append(num)
    positive_array.sort()
    return positive_array


def get_first_missing_positive(array):
    array = remove_neg_and_arrange(array)
    i = 1
    if len(array) == 0:
        return i

    for num in array:
        if i >= num:
            i += 1
    return i


assert get_first_missing_positive([3, 4, -1, 5]) == 1
assert get_first_missing_positive([1, 2, 0]) == 3
assert get_first_missing_positive([1, 2, 5]) == 3
assert get_first_missing_positive([1]) == 2
assert get_first_missing_positive([-1, -2]) == 1
assert get_first_missing_positive([]) == 1
