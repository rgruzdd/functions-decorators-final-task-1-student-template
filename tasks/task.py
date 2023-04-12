def split(data: str, sep=None, maxsplit=-1):
    if sep == None:
        sep = ' '
    res = []
    num_of_splits = 0
    while data != '':
        if data.find(sep) != -1 and ( num_of_splits < maxsplit or maxsplit == -1 ):
            new_word = data[0:data.find(sep)]
            if new_word == '':
                data = data.replace(sep, '', 1)
                res.append(new_word)
                num_of_splits += 1
                continue
            res.append(new_word)
            data = data.replace(data[0:data.find(sep)]+sep, '', 1)
            num_of_splits += 1
        else:
            res.append(data)
            break
    return res

