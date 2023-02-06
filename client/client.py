import sys 
import socket 
 
#client object. 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
 
server = input("Chat Server IP: ") 
port = input("Chat Server Port: ") 
 
try: 
    #connecting to chat server. 
    client.connect((server,int(port))) 
except socket.error as err: 
    #connection refused exception handling 
    print(err) 
    sys.exit(1) 
 
print("Connected to Chat Server") 
 
while True: 
    #client input msg. 
    msg = input("You : ") 
 
    #encoding the msg. 
    client.send(msg.encode()) 
 
    #decoding the msg from server. 
    msg = client.recv(1024).decode() 
    print(msg) 
 
client.close()
