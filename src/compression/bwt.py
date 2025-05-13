def bwt_transform(s):
    s+='$'
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations.sort()
    return ''.join(row[-1] for row in rotations)
