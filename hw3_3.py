## no libraries allowed

def reverseBwt(t):
    '''computes the inverse of the BWT, where t is a string'''

    # Construct the matrix
    matrix = []
    for i in range(len(t)):
        matrix.append(t[i:] + t[:i])
    matrix.sort()

    # Extract the first and last columns
    first_column = [row[0] for row in matrix]
    last_column = [row[-1] for row in matrix]

    # Count the occurrences of each character in the last column
    count = {}
    for char in last_column:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Compute the starting positions of each character in the first column
    starts = {}
    total = 0
    for char, freq in sorted(count.items()):
        starts[char] = total
        total += freq

    # Reconstruct the original string
    index = starts['$']
    result = ['$']
    while len(result) < len(t) + 1:
        char = first_column[index]
        index = starts[char] + first_column[:index].count(char)
        result.append(char)
    return ''.join(result[::-1])



f = open("hw3_test3.txt", "r")         # open the file
text = f.readline().strip()            # text is on the first line
print(reverseBwt(text))                # expected output TACATCACGT$