import socket
import threading

class ChatServer:
    def __init__(self):
        """
        Clase para el servidor de chat.
        """
        self.host = 'localhost'
        self.port = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        """
        Transmite un mensaje a todos los clientes conectados.
        :param message: El mensaje a transmitir.
        """
        for client in self.clients:
            client.send(message)

    def handle_client(self, client):
        """
        Maneja la conexión de un cliente individual.
        :param client: El socket del cliente conectado.
        """
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                # Si hay un error al recibir datos del cliente, se cierra la conexión y se elimina de la lista de clientes.
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the chat'.encode('utf-8'))
                break

    def start(self):
        """
        Inicia el servidor y acepta conexiones entrantes.
        """
        print('Server started')
        while True:
            client, address = self.server.accept()
            print(f'New connection from {address}')
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)
            print(f'Nickname of the client is {nickname}')
            self.broadcast(f'{nickname} joined the chat'.encode('utf-8'))
            client.send('Connected to the server'.encode('utf-8'))
            client.send('Start messaging'.encode('utf-8'))
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()

server = ChatServer()
server.start()
