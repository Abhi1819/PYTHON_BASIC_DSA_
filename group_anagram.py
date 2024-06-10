# group anagram.py

def ana(ls: list) -> list:
    ds = {}
    for x in ls:
        s_word = ''.join(sorted(x))
        if s_word not in ds:
            ds[s_word] = [x]
        else:
            ds[s_word].append(x)
    return ds

resp = ana(['tea', 'ate', 'king', 'gink'])
print(resp.items())
