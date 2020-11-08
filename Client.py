import socket

class Client():
    def __init__(self):
        self.client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = '127.0.0.1'#socket.gethostname()
        self.server_port = 1234 # socket server port number

    def connection_with_server(self):
        print('Waiting for connection')
        try:
           connection= (self.server_host, self.server_port)
        except socket.error as e:
            print(str(e))
        self.client_socket.connect(connection)
        print('Connection established.')
        users_credentials=0

     #   Response = self.client_socket.recv(1024)
        while True:
           if users_credentials == 0:
                name = input("Give name: ")
                self.client_socket.sendall(name.encode('utf-8'))
                if name=='bye':
                    break
                response_from_server = self.client_socket.recv(1024).decode('utf-8')
                print(response_from_server)
           users_credentials += 1

           request = input('Choose an option.\n1)Deposit.\n2)Cash-back.\n3)Exit\n')
           if 'Exit' in request:
               print('Exiting.')
               self.client_socket.sendall('{}'.format('Exit ').encode('utf-8'))
               self.client_socket.close()
               break
           self.client_socket.sendall(request.encode('utf-8'))

        self.client_socket.close()  # close the connection


if __name__ == '__main__':
    client=Client()
    client.connection_with_server()
