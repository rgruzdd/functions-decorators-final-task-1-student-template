from typing import List

def split(data: str, sep=None, maxsplit=-1):
    if sep == None:
        sep = ' '
    res = []
    new_word = ''
    for i in data:
        if i == sep:
            res.append(new_word)
            new_word = ''
        else:
            new_word += i
    res.append(new_word)
    return res

