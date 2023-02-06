import socket
import sys

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = input("Server Port : ")

try:
  server.bind(('0.0.0.0', int(port))) # bind to localhost on port 1234
except socket.error as err:
  print(err)
  sys.exit(1)

print("Server Started")
server.listen() # listen for incoming connections

# Keep track of connected clients for group chats.
clients = []

while True:
    # accept new client connections
    client, address = server.accept()
    clients.append(client)
    print(f'{address} connected')

    # receive messages from the client
    while True:

      msg = client.recv(1024).decode()
      if not msg:
          break
      # broadcast message to all connected clients
      for c in clients:
          # print(address[0]+" : "+msg)
          c.send(f'{address}: {msg}'.encode())

    client.close()
    clients.remove(client)
    print(f'{address} disconnected')

server.close()
