
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


#This is a modified version of the code from 10.6
def romeo2(fname):
    fhand = open(fname)
    count = {}
    t = []
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        for word in words:
            count[word] = count.get(word, 0) + 1
    for key, val in count.items():
        t.append((val, key))
    t.sort(reverse=True)
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


#Modified for Chapter 10 Exercise 1
def maillog(fname):
    fhand = open(fname)
    md = {}
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        md[words[1]] = md.get(words[1], 0) + 1
    print(md)

    t = []
    for key, val in md.items():
        t.append((val, key))
    t.sort(reverse=True)
    print(t[0])

    #Exercise 4 chapter 9
    #largest = 0
    #mail = ''
    #for x in md:
    #    if md[x] > largest:
    #        largest = md[x]
    #        mail = x
    #print(mail, largest)

#Exercise 2 chapter 10
def timeofday(fname):
    fhand = open(fname)
    md = {}
    for line in fhand:
        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue
        tod = words[5]
        tods = tod.split(':')
        #get the hours
        hr = tods[0]
        md[hr] = md.get(hr, 0) + 1
    #Whoops, sorted by count, exercise says sort by hour
    #t = []
    #for key, val in md.items():
    #    t.append((val, key))
    #t.sort(reverse=True)
    #for h in t:
    #    print(h[1], h[0])
    z = list(md.items())
    z.sort()
    for y in z:
        print(y[0], y[1])


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
        elif arg.lower() == 'romeo2':
            fname = 'romeo.txt'
            romeo2(fname)
        elif arg.lower() == 'time':
            fname = 'mbox-short.txt'
            timeofday(fname)

        else:
            print('I do not recognize that command: ')

