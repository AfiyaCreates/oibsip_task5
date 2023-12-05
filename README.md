# oibsip_task5

```markdown
# Simple Chat App

## Overview
This is a simple chat application implemented in Python using sockets. It consists of a server and a client that communicate with each other over a local network.

## Features
- Server-Client architecture for real-time communication.
- Exchange messages between the server and client.
- User-friendly interface for input and display of messages.

## Usage

### Server
1. Run the server script:
    ```bash
    python server.py
    ```
2. The server will bind to the specified host and port (default: 127.0.0.1:1234) and wait for a client to connect.
3. Once a client connects, the server establishes a connection and starts receiving and sending messages.

### Client
1. Run the client script:
    ```bash
    python client.py
    ```
2. Enter your username when prompted.
3. The client connects to the server and starts a chat session.
4. Type your messages in the console to send them to the server.
5. The client receives and displays messages from the server.

### Note
- To exit the chat, type "quit" when prompted for a message.

## Files
- `server.py`: The server script that listens for incoming connections and handles communication.
- `client.py`: The client script that connects to the server and participates in the chat.

## Contributing
Feel free to contribute to the project by opening issues or pull requests. Your input is valuable!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy chatting with the Simple Chat App!
```
