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
        connection_thread.sendall(str.encode('Welcome to the Server ' + client_name +'. Wait for validation.'))
        while True:
            #connection_thread.sendall(str.encode('Welcome '+ client_name))
            option = connection_thread.recv(2048).decode('utf-8')
            print('Client  option: ' + option)
            if option == '1':
                print('Withdrawal')
                connection_thread.sendall(str.encode('--WITHDRAWAL--\n Give the amount of the withdrawal: '))
                amount = int(connection_thread.recv(2048).decode('utf-8'))
                print(amount)
                #Check if the amount is valid
                if(amount > 0 and (amount%10==0)):
                    #Check if amount can be expressed in multiples of 20 and 50
                    multOf20= (amount/20 == amount//20)
                    multof50= (amount>=50 and ((amount-50)/20 == (amount-50)//20))
                    cash=[]
                    if multOf20 or multof50:
                        if not multOf20:
                            fifties = 1
                            temp = amount - 50
                            twenties = temp // 20
                            while twenties >= 5:
                                cash.append(50)
                                cash.append(50)
                                twenties -= 5
                            while fifties:
                                cash.append(50)
                                fifties -= 1
                        else:
                            twenties = amount // 20
                        while twenties:
                            cash.append(20)
                            twenties -=1
                        print(sorted(cash))
                        listToStr = ' '.join(map(str, cash))
                        connection_thread.sendall(str.encode(listToStr))
                    else:
                        connection_thread.sendall(str.encode('Amount can not be expressed in multiples of 20 and 50.'))
                        print('Amount can not be expressed in multiples of 20 and 50.')
                else:
                    connection_thread.sendall(str.encode('Invalid amount.'))
                    print('Client gave invalid amount.')
            elif option == '2':
                print('Deposit')
                connection_thread.sendall(str.encode('--DEPOSIT--\n Give the amount of the deposit: '))
                amount = int(connection_thread.recv(2048).decode('utf-8'))
                if (amount <= 0 ) or (amount % 5 != 0):
                    connection_thread.sendall(str.encode('Invalid amount.'))
                    print("Client gave invalid amount.")
                    break
                else:
                    connection_thread.sendall(str.encode('Deposit is done.'))
                    print("Deposit is done.")
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
                connection_thread.sendall(str.encode('Something went wrong\n'))
                print('Something went wrong.')


    def validate_user(self, user, password):
        pass

    def get_account(self, amount, user_id):
        pass

    def update_account(self, amount, user_id):
        pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
