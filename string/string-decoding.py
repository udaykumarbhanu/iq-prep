def decoding(s):
    if not s: return s

    result = []
    count = 0

    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result.append(char * count)
            count = 0

    return ''.join(result)

if __name__ == '__main__':
    s = "12a2p1l1e"

    print decoding(s)
