import socket
import threading


class Server(object):
    def __init__(self):
        #create lock
        self.lock=threading.Lock()
        # get the hostname
        self.host = '127.0.0.1' #socket.gethostname()
        self.port = 1234  # initiate port no above 1024
        print ("[+] New server socket thread started for " + self.host + ":" + str(self.port) )


    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        print('Server started. Waiting for a Connection..')
        # configure how many client the server can listen simultaneously
        server_socket.listen(1)

        while True:
             #accept client
             connection, address = server_socket.accept()
             print('Connected to: ' + address[0] + ':' + str(address[1]))
             newthread= threading.Thread(target=self.threaded_client, args=(connection,)) # start_new_thread(threaded_client, (conn,))
             newthread.start()

        server_socket.close()


    def threaded_client(self, connection_thread):
        client_name = connection_thread.recv(2048).decode('utf-8')
        client_password = connection_thread.recv(2048).decode('utf-8')

        # elegxos an uparxei stn vasi

        print('Client ' +client_name + """ connected to the server. Waiting for client's option""")
        print(client_password)
        connection_thread.sendall(str.encode('Welcome to the Server ' + client_name +'. Wait for validation.'))
        while True:
            #connection_thread.sendall(str.encode('Welcome '+ name_option))
            option = connection_thread.recv(2048).decode('utf-8')
            print('Client  option: ' + option)
            if option == '1':
                print('Withdrawal')
                connection_thread.sendall(str.encode('--WITHDRAWAL--\n Give the amount of the withdrawal: '))
                amount = connection_thread.recv(2048).decode('utf-8')
                if(amount <=0):
                    connection_thread.sendall(str.encode('Invalid amount.'))
                    print("Client gave invalid amount.")
                #Check if amount can be expressed in multiples of 20 and 50

                pass
            elif option == '2':
                print('Deposit')
                connection_thread.sendall(str.encode('--DEPOSIT--\n Give the amount of the deposit: '))
                amount = connection_thread.recv(2048).decode('utf-8')
                if (amount <= 0 ) or (amount % 5 == 2):
                    connection_thread.sendall(str.encode('Invalid amount.'))
                    print("Client gave invalid amount.")
                    break
                #Check the database
                # if():
                #     connection_thread.sendall(str.encode('Take your money'))
                # else:
                #     connection_thread.sendall(str.encode('You done have enough money.'))
                #
                pass
            elif option == '3':
                print('Balance')
                pass
            elif option == '4':
                print('Client exited.Session terminated.')
                break
            else:
                print('Something went wrong.')
                connection_thread.sendall(str.encode('Something went wrong\n'))

    def validate_user(self, user, password):
        pass

    def get_account(self, amount, user_id):
        pass

    def update_account(self, amount, user_id):
        pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
