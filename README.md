# Network Tic Tac Toe

A multiplayer Tic Tac Toe game implemented with Python socket networking.  
The project demonstrates a simple client-server architecture, allowing two players to compete over a network connection.


## Features
- Server–Client architecture using Python sockets  
- Real-time two-player gameplay  
- Command-line interface for both client and server  
- Modular design separating logic, networking, and UI components  


## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/eslamelhosuniy/Network-Tic-Tac-Toe.git
cd Network-Tic-Tac-Toe 
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the server
```bash
python server/server.py
```
### 4. Run the client
```bash
python client/client.py
```

# Technologies Used

- Python 3.10+  
- Socket programming  
- Threading  



# Architecture Overview

The system follows a simple client-server model:

1. The **server** hosts the game logic and manages active sessions.  
2. Each **client** connects to the server using TCP sockets.  
3. Clients send and receive JSON-formatted messages terminated by newline characters.  
4. The **server** updates the game state and broadcasts it to both clients in real-time.  

Example message flow:
```json
Client X -> Server: {"action": "move", "pos": 4}
Server -> Both Clients: {"state": ["X","O"," "," ","X"," "," "," ","O"], "turn": "O"}
