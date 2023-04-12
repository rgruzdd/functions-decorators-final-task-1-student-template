from typing import List

def split(data: str, sep=None, maxsplit=-1):
    res = []
    new_word = ''
    for i in data:
        if i != ' ':
            new_word += i
        else:
            i = ' '
            res.append(new_word)
            new_word = ''
    res.append(new_word)
    return res
