import zmq

context=zmq.Context()
socket=context.socket(zmq.REP)
socket.bind('node01:5556')

while True:
    msg=socket.recv()
    print('From client: '),msg
    smsg=input('Enter your message here: ')
    socket.send(smsg)
    print('')