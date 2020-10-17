"""
Example:
persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
"""

n = 39
count = 0


def product(n):
    res = 1
    while n != 0:
        res = res * (n % 10)
        n = n // 10
    return res


while len(str(n)) > 1:
    n = product(n)
    count += 1

print(count)
