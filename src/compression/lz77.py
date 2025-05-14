def lz77_compress(s):
    if not s:
        print("empty string")
        return ""
    
    end = len(s)
    result = []
    i = 0
    while i < end :
        offset = 0
        length = 0

        for j in range(i):
            match_len = 0
               
            while( i + match_len < end and s[j+match_len] == s[i+match_len]):
                match_len +=1
            if match_len > length:
                offset = i - j
                length = match_len

        if length > 0 and i + length < end:
            c = s[i + length]
            result.append((offset, length, c))    
            i += length + 1
        elif length > 0:
           break
        else:   
            result.append((0, 0, s[i]))
            i += 1

           
    return result
        
print(lz77_compress("aaabbbccc"))




