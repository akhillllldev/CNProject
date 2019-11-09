import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
print 'A: sending HELLO to server'
name = sys.argv[-1]
clientsocket.send('HELLO')

connected = False
filename = name
# listen for ack
while True:
    buf = clientsocket.recv(64)
    if buf == "ack":
        # successfully connected
        connected = True
        print 'B: ack received'
        # send the name of the file being requested
        print 'C: requesting file from server'
        clientsocket.send(filename)
        file_contents = []
    if connected == True:
        # receive the contents of the file
        buf = clientsocket.recv(28678)
        if len(buf) > 0:
            print 'D: file received from server'
            file_contents.append(buf)

        file_contents_to_write = ''.join(file_contents)
        file = open('destination_folder/' + name, 'wb+')
        file.write(file_contents_to_write)
        file.close()
        print 'D: file saved in destination folder'
        print 'E: sending ack back to server'
        clientsocket.send('ack')
        break
