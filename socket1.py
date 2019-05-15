import socket


#C12 Exercise 1
url = input('Enter url - ')


#C12 Exercise 5, only show data after the headers and a new line have been received

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
    #c12e5 initialize empty line and clean printed text vars
    eol = 0
    toprint = ''

    while True:
        data = mysock.recv(512)
        ddata = data.decode()
        #c12e5 check for empty line and set var
        if '\r\n\r\n' in ddata:
            eol = 1
            pos = ddata.find('\r\n\r\n')
            #split the data because empty line could be in middle of data
            #we only want second half, no headers
            #we will keep one \r\n in for formatting though.
            ddata = ddata[pos + 2:]
        if eol == 1:
            toprint += ddata
        if len(data) < 1: break
        count = count + len(data)
        #if count < 3000:
        #    print(len(data), count)
    print(toprint)
    print('Total number of characters: {}'.format(count))
        #print(data.decode(),end='')

    mysock.close()
except:
    print('Bad URL, please try again')

