# server/serverExceptions.py

class ServerError(Exception):
    pass

class PlayerDisconnectedError(ServerError):
    def __init__(self, player_addr, message="Player disconnected"):
        self.player_addr = player_addr
        super().__init__(f"{message}: {player_addr}")

class PlayerQuitError(ServerError):
    def __init__(self, player_addr, message="Player quit"):
        self.player_addr = player_addr
        super().__init__(f"{message}: {player_addr}")

class InvalidMessageError(ServerError):
    def __init__(self, player_addr, message="Invalid message"):
        self.player_addr = player_addr
        super().__init__(f"{message}: {player_addr}")

class TimeoutWaitingPlayerError(ServerError):
    def __init__(self, player_addr, message="Timeout waiting for player"):
        self.player_addr = player_addr
        super().__init__(f"{message}: {player_addr}")
