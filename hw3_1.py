## no libraries allowed

def suffixArray(t):
    """computes the suffix array of string t by sorting all suffixes of t"""
    ## YOUR CODE HERE
    ## YOUR CODE HERE
    suffixes = []
    for i in range(len(t)):
        suffixes.append((t[i:], i))
    suffixes.sort(key=lambda a: a[0])

    t = ''
    for suffix in suffixes:
        t += str(suffix[1]) + ' '

    return t

f = open("hw3_test1.txt", "r")         # open the file
text = f.readline().strip()            # text is on the first line
print(text)
s = suffixArray(text)                  
print(''.join(map(str,s)))            # expected output 15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
