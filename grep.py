import re

#Exercise 1
def grepit(fname, regex):
    hand = open(fname)
    count = 0
    for line in hand:
        line = line.rstrip()
        if re.search(regex, line):
            count += 1
    print('{0} had {1} lines that matched {2}'.format(fname, count, regex))

#Exercise 2 & 3
def newrev(fname):
    hand = open(fname)
    for line in hand:
        line = line.rstrip()
        #Exercise 2
        if re.search('^New Revision:', line): 
            print(line)
        #exercise 3
        mat = re.findall('^New Revision: ([0-9.]+)', line)
        if len(mat) > 0:
            print(mat)


if __name__ == '__main__':
    while True:
        arg = input('Select your function, or type done to exit: ')
        if arg.lower() == 'done':
            break
        elif arg.lower() == 'grepit':
            #Exercise 1
            regex = input('Give me a regular expression: ')
            fname = 'mbox-short.txt'
            grepit(fname, regex)
        elif arg.lower() == 'newrev':
            fname = 'mbox-short.txt'
            newrev(fname)

