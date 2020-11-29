import socket

# creates a new TCP socket,IPV4
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# asking user for url
url = input('Enter url: ')

# to catch errors
try:
    # splits with '/' and finds the host name
    host = url.split('/')[2]

    # connects to the host
    mysock.connect((host, 80))

    # sending a GET request
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    # response loop
    while True:
        # recieving response of 512 bytes
        data = mysock.recv(512)

        # checking if reponse is empty,if true then stop the loop
        if len(data) < 1:
            break

        # prints the current reponse without newline
        print(data.decode(), end='')

    # closing the socket
    mysock.close()

# index error indicates invalid '/' characters and its not a url
except IndexError:
    print('Invalid URL: ', url)

# socket.gaierror indicates trying to connect a non existing host/service
except socket.gaierror:
    print('invalid host name: ', host)