import zmq

context= zmq.Context()
socket=context.socket(zmq.REQ)
socket.connect("node01:5556")

while True:
    msg=input('Enter your message: ')
    socket.send(msg)
    print('sending... '),msg
    print('From server : '), socket.recv()
    print('')