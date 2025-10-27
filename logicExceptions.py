# logic/logicExceptions.py

class InvalidMoveError(Exception):
    """Raised when a move input is invalid (e.g., not a number 0–8)."""
    pass

class OutOfRangeError(Exception):
    """Raised when the move position is outside the board range (0–8)."""
    pass

class CellOccupiedError(Exception):
    """Raised when a player tries to play in an already occupied cell."""
    pass

class NotYourTurnError(Exception):
    """Raised when a player attempts to play out of turn."""
    pass

class GameOverError(Exception):
    """Raised when attempting to play after the game has already ended."""
    pass

class PlayerNotRecognizedError(Exception):
    """Raised when the player making the move is not recognized."""
    pass
