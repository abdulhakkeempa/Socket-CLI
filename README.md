# Socket-CLI

```
  ____   ___   ____ _  _______ _____    ____ _     ___ 
 / ___| / _ \ / ___| |/ / ____|_   _|  / ___| |   |_ _|
 \___ \| | | | |   | ' /|  _|   | |   | |   | |    | | 
  ___) | |_| | |___| . \| |___  | |   | |___| |___ | | 
 |____/ \___/ \____|_|\_\_____| |_|    \____|_____|___|
```

The application utilizes socket programming to create a client-server connection, where clients can connect to the server to start a chat session.

The chat experience is purely text-based and users can type in messages to send to the other connected clients. The server is responsible for maintaining a list of all connected clients and forwarding messages between them in real-time. The application is designed to be lightweight and fast, making it easy for users to chat with each other without any lag or delays.

The CLI Chat Application is perfect for individuals who want a simple way to communicate with others over a network. Whether you're working with a team, connecting with friends, or just need a quick way to send messages, the CLI Chat Application provides a fast and reliable solution. With its simple and straightforward design, you can get started chatting in no time.

This application will only work in the same network.

### Running the application
1. Clone the repository that contains the chat application.
2. On the device that will act as the chat server, run the file ```server/server.py```. You'll need to provide the port number that the server will listen on.
3. On each device that will act as a chat client, run the file ```client/client.py```. You'll need to provide the public IP address of the server and the port number that the server is listening on.
4. Once the client is connected to the server, you can start chatting with other connected clients. Enjoy endless communications! 💬

Note: It is important to make sure that the server's firewall is configured to allow incoming connections on the port used by the chat application and that the client is connecting to the correct public IP address of the server.

### Common Errors
1. Firewall Configuration: On the server & chat device, make sure that the firewall is configured to allow incoming & outgoing connections on the port used by the chat application.
2. Dynamic IP Address: Public IP addresses may change over time, so confirm the public IP address of the server and ensure that the client is connecting to the correct address.

### Issues

If you encounter any bugs or issues while using this chat application, please open a new issue in this repository. When opening a new issue, please include the following information:

1. A clear and concise description of the problem you're facing.  
2. Steps to reproduce the issue, if possible.  
3. Any relevant logs, error messages, or screenshots.  
4. The operating system and version you're running on.  

By providing this information, you'll help us resolve the issue as quickly as possible. Thank you for taking the time to report any issues you encounter while using this chat application.






