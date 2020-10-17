# arra= [10, -80, 10, 10, 15, 35]
# arr = [1, 2, 3, 4, 3, 2, 1]
# arr = [1, 2, 3, 4, 5, 6]
arr = [10, -80, 10, 10, 15, 35, 20]


def find_even_index(array):
    """поиск позиции элемента, сумма справа от которго равна сумме слева, моя версия"""
    i, result = 0, -1
    while i <= len(array):
        if array[i - 1]:
            if sum(array[:i - 1]) == sum(array[i:]):
                result = i - 1
        if i == 0:
            if sum(array[i:]) == 0:
                result = 0
        i += 1
    return result


print(f'result: {find_even_index(arr)}')

# топовое решение с codewars
# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1
