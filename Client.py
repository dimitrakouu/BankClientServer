import socket
from getpass import getpass

class Client(object):
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
                name = input("Give username: ")
                self.client_socket.sendall(name.encode('utf-8'))
                password = input("Give password: ")
                self.client_socket.sendall(password.encode('utf-8'))
                #after the validation is done:
                response_from_server = self.client_socket.recv(1024).decode('utf-8')
                print(response_from_server)
           users_credentials += 1
           request = input('Choose an option.\n1)Withdrawal.\n2)Deposit.\n3)Balance.\n4)Exit.\n')
           if '4' == request: #exit
               print('Exiting.')
               self.client_socket.sendall('{}'.format('Exit ').encode('utf-8'))
               self.client_socket.close()
               break
           self.client_socket.sendall(request.encode('utf-8'))
           if request == '1': #withdrawal
               response_from_server = self.client_socket.recv(1024).decode('utf-8')
               print(response_from_server)
               amount = input()
               # send the amount to server
               self.client_socket.sendall(amount.encode('utf-8'))
               # take the respone and print it
               response_from_server = self.client_socket.recv(1024).decode('utf-8')
               print(response_from_server)
               pass
           elif request == '2': #deposit
               response_from_server = self.client_socket.recv(1024).decode('utf-8')
               print(response_from_server)
               amount=input()
               #send the amount to server
               self.client_socket.sendall(amount.encode('utf-8'))
               #take the respone and print it
               response_from_server = self.client_socket.recv(1024).decode('utf-8')
               print(response_from_server)
               pass
           elif request == '3': #balance
               #take balance from server and print
               #response_from_server = self.client_socket.recv(1024).decode('utf-8')
               #print(response_from_server)
               pass
           else:
               response_from_server = self.client_socket.recv(1024).decode('utf-8')
               print(response_from_server)


        self.client_socket.close()  # close the connection


if __name__ == '__main__':
    client=Client()
    client.connection_with_server()
