import urllib.request, urllib.parse, urllib.error

url = input('Enter a url - ')

try:
    img = urllib.request.urlopen(url)
    count = 0 
    while True:
        data = img.read(512)
        if len(data) < 1: break
        count = count + len(data)
        if count < 3000:
            print(count)
    print('Total character count: {}'.format(count))



except Exception as e:
    #print('Bad URL, try again')
    print(e)
