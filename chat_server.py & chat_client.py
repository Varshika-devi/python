import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(1)

print("Waiting for connection...")
client, addr = server.accept()
print("Connected:", addr)

while True:
    msg = client.recv(1024).decode()
    print("Client:", msg)
    reply = input("You: ")
    client.send(reply.encode())


import socket

client = socket.socket()
client.connect(("localhost", 9999))

while True:
    msg = input("You: ")
    client.send(msg.encode())
    reply = client.recv(1024).decode()
    print("Server:", reply)
