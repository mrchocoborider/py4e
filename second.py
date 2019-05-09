
def chop(t):
    del t[-1]
    del t[0]
    print(t)
    return None

def middle(t):
    x = t[1:-1]
    return x

def romeo(fname):
    fhand = open(fname)
    t = []
    for f in fhand:
        f = f.split()
        for i in f:
            if i in t: continue
            else: t.append(i)
    t.sort()
    print(t)
                
def frmfinder(fname):
    fhand = open(fname)
    count = 0
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        print(words[1])
        count += 1
    print('There were {0} line in the file with From as the first word'.format(count))

#count days of the week on lines that start with from
def frmfinder2(fname):
    fhand = open(fname)
    dowd = {}
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        dowd[words[2]] = dowd.get(words[2], 0) + 1
    print(dowd)

def maillog(fname):
    fhand = open(fname)
    md = {}
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        md[words[1]] = md.get(words[1], 0) + 1
    print(md)

    #Exercise 4 chapter 9
    largest = 0
    mail = ''
    for x in md:
        if md[x] > largest:
            largest = md[x]
            mail = x
    print(mail, largest)

#Exercise 5
def schoolcount(fname):
    fhand = open(fname)
    sc = {}
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        split = words[1].find('@') + 1
        #get everything after the @
        s = words[1][split:]
        sc[s] = sc.get(s, 0) + 1
    print(sc)


if __name__ == '__main__':
    while True:
        arg = input('Select your function, or type done to exit: ')
        if arg.lower() == 'done':
            break
        elif arg.lower() == 'chop':
            #not gonna do safety checks since I'll be entering the list
            t = input('Give me a list, python style: ')
            t = eval(t)
            chop(t)
        elif arg.lower() == 'middle':
            #not gonna do safety checks since I'll be entering the list
            t = input('Give me a list, python style: ')
            t = eval(t)
            x = middle(t)
            print(x)
        elif arg.lower() == 'romeo':
            fname = 'romeo.txt'
            romeo(fname)
        elif arg.lower() == 'frmfinder':
            fname = 'mbox-short.txt'
            frmfinder(fname)
        elif arg.lower() == 'frmfinder2':
            fname = 'mbox-short.txt'
            frmfinder2(fname)
        elif arg.lower() == 'maillog':
            fname = 'mbox-short.txt'
            maillog(fname)
        elif arg.lower() == 'schoolcount':
            fname = 'mbox-short.txt'
            schoolcount(fname)

        #elif arg.lower() == 'spamconf':
        else:
            print('I do not recognize that command: ')

