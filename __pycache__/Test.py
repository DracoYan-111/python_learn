import doctest 

def add(a, b):
 add(2, 3)
 return a + b
doctest.testmod()

import doctest


def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    """
    return a * b

doctest.testmod()

# 编程文件中的 Doctests
def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2

    >>> count_vowels('Manila')
    3
    """
    total_vowels = 0
    for letter in word:
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels

if __name__ == "__main__":
    import doctest
    doctest.testmod()