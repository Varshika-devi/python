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
