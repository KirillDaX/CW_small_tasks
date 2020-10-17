"""
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

example_word = 'abba'
example_words = ['aabb', 'abcd', 'bbaa', 'dada']


def anagrams(word: str, words: list) -> list:
    result = []
    for item in words:
        if len(item) == len(word):
            if set(item) == set(word):
                result.append(item)
    return result


print(anagrams(example_word, example_words))
