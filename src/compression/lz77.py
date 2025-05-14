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
                match_len += 1
            if match_len > length:
                offset = i - j
                length = match_len

        if length > 0 and i + length < end:
            char = s[i + length]
            result.append((offset, length, char))    
            i += length + 1
        elif length > 0:
            result.append((offset, length, ""))
            break
        else:   
            result.append((0, 0, s[i]))
            i += 1

           
    return result
        
def lz77_decompress(data):
    if not data:
        print("empty")
        return
    
    result = ""

    for offset, length, char in data:
        if offset == 0 and length == 0:
            result += char
        else:
            start = len(result) - offset
            end = start + length
            while start < end:
                result += result[start]
                start += 1
            result += char
    return result

text = "jjuurrnn,,[[]][]][][]"
print(lz77_compress(text))
print(lz77_decompress(lz77_compress(text)))





