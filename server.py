import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1234
server.bind((host,port))
server.listen()
client,address=server.accept()

client_username = client.recv(1024).decode('utf-8')
print(f"Connection established with {client_username}")
server_name = "ChatServer"
client.send(server_name.encode('utf-8'))

done=False
while not done:
   msg= client.recv(1024).decode('utf-8')
   if msg =="quit":
     done=True
   else:
     print(f"{client_username}: {msg}")
   response = input("Message: ")   
   client.send(response.encode('utf-8'))
   
client.close()
server.close()