"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}
"""

# без  counta:
data = 'abrakadabra'
res = {}
print(list(data))
for item in list(data):
    if item not in res:
        res[item] = 1
    else:
        res[item] += 1
print(res)
#  через count в одну строку
print({item: data.count(item) for item in data})
