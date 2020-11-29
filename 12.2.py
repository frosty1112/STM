import socket
url = input('Enter: ')
try:
    words = url.split('/')
    host = words[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())
    n=''
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        n=n+(data.decode())
      
    print(n[:3001])
    print('Total number of characters',len(n))
    mysock.close()
except:
    print('not formatted properly')