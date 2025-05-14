def bwt_transform(s):
    s+='$'
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations.sort()
    return ''.join(row[-1] for row in rotations)

def bwt_inverse(s):
    n = len(s)
    table = [''] * n
    for _ in range(n):
        table = sorted(s[i] + table[i] for i in range(n))
    return table[table.index('$')].replace('$', '')
