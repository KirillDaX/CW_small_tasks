# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

import re
from re import sub
# s = "example(unwanted thing)example"
# s = 'hello example (words(more words) here) something'
# s = '(first group) (second group) (third group)'
# s = 'hello example (words(more words) here) something'
s = '1 ( 2 ( 3 ) 4 ( 5 ) 6 7) ?'

start_parenthes = s.find('(')
end_parenthes = s.rfind(')')
cut_part = s[start_parenthes:end_parenthes + 1]
out_data = s.replace(cut_part, '')

one_line_out = s.replace(s[s.find('('):s.rfind(')') + 1], '')  # по ТЗ соотвествует
print(f'out1 = ({one_line_out})')  # такой вывод чтобы видеть кол-во пробелов.
# 3ий  пример выыполняется не по задумке автора, должно остаться два пробела.

# доп мысль
# while '(' in s:
#     if s.rfind('(') < s.find(')'):
#         out = s.replace(s[s.rfind('('):s.find(')') + 1], '')
#     else:
#         out = s.replace(s[s.find('('):s.find(')') + 1], '')
#     s = out
#
# print(f'out2 = ({out})')


def remove_parenthes(text):  # через регулярки
    n = 1  # 1 run
    while n:
        text, n = re.subn(r'\([^()]*\)', '', text)
    return text


def remove_parenthes2(s):
    while '(' in s:
        s = sub('\([^()]*\)', '', s)
    return s


print(f'func1 = ({remove_parenthes(s)})')
print(f'func2 = ({remove_parenthes2(s)})')
