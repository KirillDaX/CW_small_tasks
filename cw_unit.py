example = [2, 4, 0, 100, 4, 11, 2602, 36]


def find_outlier(data):
    """если в массиве четных чисел есть нечетное выведет его, и ноборот."""
    array1 = []
    array2 = []

    for item in data:
        if item % 2 == 0:
            array1.append(item)
        else:
            array2.append(item)

    if len(array1) > len(array2):
        return array2[0]
    else:
        return array1[0]
