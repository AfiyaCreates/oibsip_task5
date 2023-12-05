import socket

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1234
client.connect((host,port))

username = input("Enter your username: ")
client.send(username.encode('utf-8'))
server_name = client.recv(1024).decode('utf-8')
print(f"Connected to {server_name}")

done= False
while not done:
    client.send(input("Message:").encode('utf-8'))
    msg= client.recv(1024).decode('utf-8')
    if msg.lower()=="quit":
        done= True
    else:
        print(f"{server_name}: {msg}")

        
        
client.close()           
