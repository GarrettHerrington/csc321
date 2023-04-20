import zmq

context= zmq.Context()
socket=context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5556")

while True:
    msg=input('Enter your message: ')
    socket.send(msg)
    print('sending... '),msg
    print('From server : '), socket.recv()
    print('')