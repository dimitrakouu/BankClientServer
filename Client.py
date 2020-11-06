import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    print('Waiting for connection')
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(str(e))
   # client_socket.connect((host, port))  # connect to the server

    Response = client_socket.recv(1024)
    while True:
        Input = input('Say Something: ')
        client_socket.send(str.encode(Input))
        Response = client_socket.recv(1024)
        print(Response.decode('utf-8'))

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
