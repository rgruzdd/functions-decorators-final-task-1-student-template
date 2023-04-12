from typing import List

def split(data: str, sep=None, maxsplit=-1):
    res = []
    new_data = data
    if sep is not None:
        new_data = data.replace(sep, ':')
    else:
        sep = ' '
    num_of_splits = 0
    new_word = ''
    for i in new_data:
        if i != ':':
            new_word += i
        else:
            if maxsplit == -1:
                if new_word != '':
                    res.append(new_word)
                new_word = ''
            elif num_of_splits < maxsplit:
                if new_word != '':
                    res.append(new_word)
                new_word = ''
                num_of_splits += 1
            else:
                new_word += i

    if new_word is not None:
        res.append(new_word)
    return res


