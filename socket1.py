import socket


#C12 Exercise 1
url = input('Enter url - ')

try:
    prts = url.split('/')
    hst = prts[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hst, 80))
    cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(url).encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print('Bad URL, please try again')

