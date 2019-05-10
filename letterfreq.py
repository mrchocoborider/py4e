import string

#Find letters in a text and print in decreasing order of frequency
def findFreq(fname):
    fhand = open(fname)
    #ltrs = string.ascii_lowercase
    #prepare whitespace/punctuation for deletion
    todel = string.whitespace + string.punctuation + string.digits
    #print(ltrs)
    ltrd = {}
    for line in fhand:
        #remove punctuation,digits and spaces
        line = line.translate(line.maketrans('', '', todel))
        line = line.lower()
        for c in line:
            ltrd[c] = ltrd.get(c, 0) + 1

    ltrl = []
    for key, val in ltrd.items():
        ltrl.append((val, key))

    ltrl.sort(reverse = True)

    for t in ltrl:
        print(t[1], t[0])


if __name__ == '__main__':
    fname = 'mbox-short.txt'
    findFreq(fname)
