
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
        #elif arg.lower() == 'shout':
        #elif arg.lower() == 'spamconf':
        else:
            print('I do not recognize that command: ')

