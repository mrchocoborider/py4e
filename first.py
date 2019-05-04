
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

#if __name__ == '__main__':
#    average()

if __name__ == '__main__':
    minmax()
