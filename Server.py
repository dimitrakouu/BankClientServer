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
        print('Waitiing for a Connection..')
        # configure how many client the server can listen simultaneously
        server_socket.listen(5)
        threads=[]

        while True:
             #accept client
             connection, address = server_socket.accept()
             print('Connected to: ' + address[0] + ':' + str(address[1]))
             newthread= threading.Thread(target=self.threaded_client, args=(connection,)) # start_new_thread(threaded_client, (conn,))
             newthread.start()
         #    print('Thread Number: ' + threading.current_thread().name())
          #   threads.append(newthread)
        server_socket.close()


        # for i in threads:
        #     i.join()


    def threaded_client(self, connection_thread):
        name_option = connection_thread.recv(2048).decode('utf-8')
        connection_thread.sendall(str.encode('Welcome to the Server ' + name_option))
        while True:
            #connection_thread.sendall(str.encode('Welcome '+ name_option))
            option = connection_thread.recv(2048).decode('utf-8')
            print('Client  option: ' + option)
            if 'EXIT' in option.upper():
                print('Session terminated.')
                break
            elif 'VALIDATION' in option.upper():
                print('Validation')
                pass
            elif 'BALANCE' in option.upper():
                print('Balance')
                pass
            elif 'CASH_BACK' in option.upper():
                print('Cash back')
                pass
            else:
                print('sth went wrong.')
              #  connection_thread.sendall('sth went wrong'.encode('utf-8'))
                connection_thread.sendall(str.encode('Sth went wrong\n'))

    def validate_user(self, user, password):
        pass

    def get_account(self, amount, user_id):
        pass

    def update_account(self, amount, user_id):
        pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
