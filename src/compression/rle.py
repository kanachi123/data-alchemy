def rle_compress(s):
    
    
    if not s:
        print("empty string")
        return ""
    
    result = ""
    count = 1
    end =  len(s)

    for i in range(1,end):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result+=s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    
    return result


def rle_extract(s):
    if not s:
        print("emtpy string")
        return ""

    result = ""
    i = 0
    end  = len(s)
    for i in range(end):
        char = s[i]
        i+=1
        count = 0
        while i < end and s[i].isdigit():
            count = count * 10 + int(s[i])
            i+=1
        result +=char * count

    return result

t = input("input text\n")
t = rle_compress(t)
print(t)
t = rle_extract(t)
print(t) 


