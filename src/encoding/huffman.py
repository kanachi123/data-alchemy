
class Node:
    def __init__(self,char,count):
        self.char = char
        self.count = count
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.count < other.count


def count_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def huffman_tree(text):
    counts = count_frequencies(text)
    nodes = [Node(char,count)for char,count in counts.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.count)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(None, left.count + right.count)
        merged.left = left
        merged.right = right
        nodes.append(merged)
    
    return nodes[0]


def generate_codes(node, current_code='', codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = current_code
        return codes

    generate_codes(node.left, current_code + '0', codes)
    generate_codes(node.right, current_code + '1', codes)

    return codes

def huffman_encode(text):
    if not text:
        return "", {}

    root = huffman_tree(text)
    codes = generate_codes(root)

    encoded_text = ''.join(codes[char] for char in text)

    return encoded_text, codes
