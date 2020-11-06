import socket
from _thread import *


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    ThreadCount=0

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(str(e))

  #  server_socket.bind((host, port))  # bind host address and port together
    print('Waitiing for a Connection..')
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    def threaded_client(connection):
        connection.send(str.encode('Welcome to the Server\n'))
        while True:
            data = connection.recv(2048)
            server_message= input("Server says")
            reply = 'Server Says: ' + server_message
            if not data:
                break
            connection.sendall(str.encode(reply))
        connection.close()

    while True:
        conn, address = server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (conn,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    server_socket.close()




if __name__ == '__main__':
    server_program()
