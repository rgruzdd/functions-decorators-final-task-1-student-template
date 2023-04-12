def split(data: str, sep=None, maxsplit=-1):
    if sep == None:
        sep = ' '
    res = []
    num_of_splits = 0
    if data == '':
        res.append(data)
        return res
    while data != '':
        if data.find(sep) != -1 and ( num_of_splits < maxsplit or maxsplit == -1 ):
            new_word = data[0:data.find(sep)]
            if new_word == '':
                data = data.replace(sep, '', 1)
                continue
            res.append(new_word)
            data = data.replace(data[0:data.find(sep)], '', 1)
            num_of_splits += 1
        else:
            if data.find(sep) != -1:
                data = data.replace(sep, '', 1)
            res.append(data)
            break

    return res
