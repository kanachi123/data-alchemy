def mtf_encode(s):
    if not s:
        print(s)
        return []
    alphabet = list(dict.fromkeys(s))
    result = []
    for char in s:
        index = alphabet.index(char)
        result.append(index)
        alphabet.insert(0,alphabet.pop(index))

    return result

def mtf_decode(encoded,alphabet):
    result = []
    alphabet = list(alphabet)

    for index in encoded:
        char = alphabet[index]
        result.append(char)
        del alphabet[index]
        alphabet.insert(0,char)

    return ''.join(alphabet)

