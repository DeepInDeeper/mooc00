import socket

s=socket.socket()

host =socket.gethostname()
port=1224
s.bind((host,port))
s.listen(5)
while True:
        c.addr=s.accept()
        print 'Got connection from',addr
        s.send('Thank you for your conneting')
        c.close()
