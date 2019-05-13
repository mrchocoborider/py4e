import socket


#C12 Exercise 1
url = input('Enter url - ')

try:
    prts = url.split('/')
    hst = prts[2]
    print(hst)
    print(url)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hst, 80))
    cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(url).encode()
    print(cmd)
    mysock.send(cmd)
    count = 0

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count = count + len(data)
        if count < 3000:
            print(len(data), count)
    print('Total number of characters: {}'.format(count))
        #print(data.decode(),end='')

    mysock.close()
except:
    print('Bad URL, please try again')

