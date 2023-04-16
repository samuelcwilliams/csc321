import zmq

context = zmq.Context()
client_socket = context.socket(zmq.REQ)
client_socket.connect("tcp://localhost:5555")

def send_message(message):
    client_socket.send_string(message)
    reply = client_socket.recv_string()
    return reply

while True:
    message = input(">>> ")
    reply = send_message(message)
    print("Received reply:", reply)