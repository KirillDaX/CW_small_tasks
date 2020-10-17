from collections import Counter
import numpy
import openpyxl

book = openpyxl.Workbook()
sheet = book.active

array = numpy.random.randint(1, 15, 20)
print(array)

x = Counter()
for item in array:
    x[item] += 1

sheet['a1'] = 'что'
sheet['b1'] = 'кол-во'
sheet['d1'] = 'было:'
i = 2
for item in x:
    sheet[f'a{i}'] = item
    sheet[f'b{i}'] = x[item]
    i += 1

i = 2
for elem in array:
    sheet[f'd{i}'] = elem
    i += 1

book.save('ffff.xlsx')
print(x)