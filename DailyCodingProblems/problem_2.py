import numpy

def get_multiples(array):
    product_array = list()
    # for num in array:
    #     cumulative_product *= num
    cumulative_product = numpy.prod(array)
    for num in array:
        product_array.append(cumulative_product / num)
    return product_array


assert get_multiples([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert get_multiples([3, 2, 1]) == [2, 3, 6]
