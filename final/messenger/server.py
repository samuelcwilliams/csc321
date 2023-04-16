import zmq

context = zmq.Context()
server_socket = context.socket(zmq.REP)
server_socket.bind("tcp://*:5555")

def receive_message():
    message = server_socket.recv_string()
    server_socket.send_string(message)
    return message

while True:
    message = receive_message()
    print(">>> ", message)