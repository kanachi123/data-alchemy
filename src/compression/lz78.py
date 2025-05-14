def lz78_compress(data):
    if not data:
        print("empty")
        return
    
    dictionary = {}
    result = []
    index = 1
    buffer = ""

    for char in data:
        
        new_buffer = buffer + char
        
        if new_buffer in dictionary:
            buffer += new_buffer
        
        else:
            result.append((dictionary.get(buffer, 0), char))
            dictionary[new_buffer] = index
            index += 1 
            buffer = ""

    if buffer:
        result.append((dictionary.get(buffer, 0), ""))
    return result

def lz78_decompress(data):
    if not data:
        print("empty")
        return
    dictionary = {}
    result = ""

    for index,char in data:
        tmp = dictionary.get(index, "")
        result += tmp + char
        dictionary[len(dictionary) + 1] = tmp + char
    return result

text = "BANANANANANANNAANANANANA!!!!!"

print(lz78_compress(text))
print(lz78_decompress(lz78_compress(text)))