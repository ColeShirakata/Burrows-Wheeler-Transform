## no libraries allowed

def bwt(t):
    '''computes the BWT(t), where t is a string'''
    ## YOUR CODE HERE
    ## YOUR CODE HERE
    rotations = []
    for i in range(len(t)):
        rotations.append(t[i:] + t[:i])
    rotations.sort()
    
    t = ''
    for rotation in rotations:
        t += rotation[len(rotation)-1]
        print(t)

    return t

f = open("hw3_test2.txt", "r")         # open the file
text = f.readline().strip()            # text is on the first line
print(bwt(text))                       # expected output ACTGGCT$TGCGGC