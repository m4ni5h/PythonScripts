import numpy


def get_multiples(array):
    product_array = list()
    # for num in array:
    #     cumulative_product *= num
    cumulative_product = numpy.prod(array)
    for num in array:
        product_array.append(cumulative_product / num)
    return product_array


def get_multiples_array(array):
    step_product = 1
    right_product_list = list()
    for num in array:
        step_product *= num
        right_product_list.append(step_product)

    step_product = 1
    left_product_list = list()
    for num in array[::-1]:
        step_product *= num
        left_product_list.append(step_product)
    left_product_list = left_product_list[::-1]

    output_array = list()
    for i in range(len(array)):
        num = None
        if i == 0:
            num = left_product_list[i + 1]
        elif i == len(array) - 1:
            num = right_product_list[i - 1]
        else:
            num = right_product_list[i - 1] * left_product_list[i + 1]
        output_array.append(num)

    return output_array


assert get_multiples_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert get_multiples_array([3, 2, 1]) == [2, 3, 6]
