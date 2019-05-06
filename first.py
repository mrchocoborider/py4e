
def average():
    count = 0
    total = 0
    while True:
        x = input('> ')
        if x == 'done':
            break
        else:
            try:
                x = int(x)
                count += 1
                total += x
                print(x)
            except ValueError:
                print('bad data')
    avg = total/count
    print(total, count, avg)

    

def minmax():
    largest = None
    smallest = None
    while True:
        x = input('Enter a number or enter done: ')
        if x == 'done':
            break
        else:
            try:
                x = int(x)
                if largest == None or x > largest:
                    largest = x
                if smallest == None or x < smallest:
                    smallest = x

            except ValueError:
                print('bad data')
    print(largest, smallest)

#function for accepting strings, and the letter to be counted in the given string
def lcounter(letter, word):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    return(count)

def shout(fname):
    try:
        fhand = open(fname)
    except:
        print('File could not be opened')
        exit()
    for f in fhand:
        line = f.upper()
        print(line)

def spamconf(fname):
    try:
        fhand = open(fname)
    except:
        print('File could not be opened')
        exit()
    count = 0
    total = 0
    for f in fhand:
        line = f.rstrip()
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        count += 1
        sppos = line.find(' ')
        conf = line[sppos+1: ]
        #print(conf)
        conf = float(conf)
        total = total + conf
        av = total/count
    print(count, total, av)


if __name__ == '__main__':
    while True:
        arg = input('Select your function, or type done to exit: ')
        if arg.lower() == 'average':
            average()
        elif arg.lower() == 'done':
            break
        elif arg.lower() == 'minmax':
            minmax()
        elif arg.lower() == 'counter': 
            letter = input('Give me a letter to count: ')
            word = input('Give me a word so I may count its letters: ')
            count = lcounter(letter, word)
            print(count)
        elif arg.lower() == 'shout':
            fname = input('Gimme a filename: ')
            shout(fname)
        elif arg.lower() == 'spamconf':
            fname = input('Gimme a filename: ')
            if fname == 'na na boo boo':
                print("NA NA BOO BOO TO YOU - You've been punk'd")
            else:
                spamconf(fname)
        else:
            print('I do not recognize that command: ')

