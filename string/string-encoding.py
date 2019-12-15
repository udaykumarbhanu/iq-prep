def encoding(s):
    if not s: return s

    result = []
    count = 1

    for i in range(1, len(s)+1):
        if i == len(s) or s[i] != s[i-1]:
            result.append(str(count))
            result.append(s[i-1])
            count = 1
        else:
            count += 1

    return ''.join(result)

if __name__ == '__main__':
    s = 'aaaabbc'
    print encoding(s)
