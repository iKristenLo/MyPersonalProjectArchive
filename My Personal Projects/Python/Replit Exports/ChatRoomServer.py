import socket
import threading
clients = []

def handle_client(client):
    while True:
        try:
         message = client.recv(1024).decode("utf-8")
         if message:
                print("Recieved Message",message)
                print("Emitting Message")
                #Broadcasting To All Clients Except Original Sender
                for c in clients:
                    if c != client:
                        c.send(message.encode("utf-8"))
        except:
            print("An Error Acorred Breaking Connection")
            clients.remove(client)
            client.close()
            break


def start_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("localhost",8046))
    server.listen()
    print("Server Started Waiting For Connections")

    while True:
        client, address = server.accept()
        clients.append(client)
        print("newconnection",client)
        #Create A New Thread That Runs Handle_Client For The New User
        thread = threading.Thread(target = handle_client, args = (client,) )
        thread.start()
        print("Active Connections:",threading.activeCount()-1)





if __name__ == "__main__":
    start_server()
