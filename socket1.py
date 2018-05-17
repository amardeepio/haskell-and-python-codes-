import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
cmd ='GET http://data.pr4e.org/code/romeo.txt HTTP/1.0\r\n\r\n'.encode('base64','strict')

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    dat = repr(data)
    print(data.decode('utf8','strict'))
mysock.close()
