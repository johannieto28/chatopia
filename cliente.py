import socket
import threading

class ChatClient:
    def __init__(self):
        """
        Clase para el cliente de chat.
        """
        self.host = 'localhost'
        self.port = 5000
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def receive_messages(self):
        """
        Recibe y muestra mensajes del servidor.
        """
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                print(message)
            except:
                print('Error receiving messages from the server')
                self.client.close()
                break

    def send_message(self):
        """
        Envía mensajes al servidor.
        """
        while True:
            message = input()
            self.client.send(message.encode('utf-8'))

    def start(self):
        """
        Inicia el cliente y los hilos para recibir y enviar mensajes.
        """
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send_message)
        send_thread.start()

client = ChatClient()
client.start()
