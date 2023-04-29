## no libraries allowed

def reverseBwt(t):
    '''computes the inverse of the BWT, where t is a string'''

    # Construct the matrix
    rotations = []
    for i in range(len(t)):
        rotations.append(t[i:] + t[:i])
    rotations.sort()


    first_column = []
    last_column = []
    first_count = {}
    last_count = {}
    for row in rotations:
        first_char = row[0]
        if first_char in first_count:
            first_count[first_char] += 1
            first_column.append((first_char, first_count[first_char]))
        else:
            first_count[first_char] = 1
            first_column.append((first_char, first_count[first_char]))

    for letter in t:
        if letter in last_count:
            last_count[letter] += 1
            last_column.append((letter, last_count[letter]))
        else:
            last_count[letter] = 1
            last_column.append((letter, last_count[letter]))


    length = len(t)
    t = ''
    index = 0
    while len(t) < length:
        for i in range(len(first_column)):
            if first_column[index] == last_column[i]:
                index = i
                t += first_column[index][0]
                break
    
    return t



f = open("hw3_test3.txt", "r")         # open the file
text = f.readline().strip()            # text is on the first line
print(reverseBwt(text))                # expected output TACATCACGT$