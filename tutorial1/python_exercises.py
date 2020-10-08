"""
Intro to python exercises shell code
"""


def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x % 2 == 1:
        return True
    return False


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    if word[::-1] == word[::1]:
        return True
    return False


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    result = []
    for i in numlist:
        if is_odd(i):
            result.append(i)

    return result


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """

    text = text.lower().split(" ")
    result = dict.fromkeys(text, 0)
    for i, j in result.items():
        result[i] = sum(i == w for w in text)

    return result


print(only_odds([1, 2, 3, 4, 5, 6]))
print(is_palindrome("word"))
print(is_palindrome("rar"))
count_words("I love you and that is it")