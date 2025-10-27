# logic/logic.py
from logic.logicExceptions import (
    InvalidMoveError,
    OutOfRangeError,
    CellOccupiedError,
    NotYourTurnError,
    GameOverError,
    PlayerNotRecognizedError
)

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [" "] * 9
        self.players = [player1, player2]
        self.symbols = {player1: "X", player2: "O"}
        self.turn = player1
        self.winner = None

    def print_board(self):
        def cell(i):
            return f"  {self.board[i] if self.board[i] != ' ' else ' '}  "
        
        line = "_____|_____|_____"
        empty_line = "     |     |     "
        
        return (
            f"\n{empty_line}\n"
            f"{cell(0)}|{cell(1)}|{cell(2)}\n"
            f"{line}\n"
            f"{empty_line}\n"
            f"{cell(3)}|{cell(4)}|{cell(5)}\n"
            f"{line}\n"
            f"{empty_line}\n"
            f"{cell(6)}|{cell(7)}|{cell(8)}\n"
            f"{empty_line}\n\n"
        )

    def check_winner(self):
        combos = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                self.winner = self.board[a]
                return self.winner
        if " " not in self.board:
            self.winner = "Draw"
            return self.winner
        return None

    def make_move(self, player, move):
        # move is expected to be a string representing digit (e.g., "4")
        if player not in self.players:
            raise PlayerNotRecognizedError("Unknown player.")

        if self.winner:
            raise GameOverError("The game is already over!")

        if player != self.turn:
            raise NotYourTurnError("It's not your turn!")

        if not isinstance(move, str) or not move.isdigit():
            raise InvalidMoveError("Move must be a string digit between 0 and 8.")

        move = int(move)
        if not (0 <= move <= 8):
            raise OutOfRangeError("Move must be between 0 and 8.")

        if self.board[move] != " ":
            raise CellOccupiedError("This cell is already taken!")

        self.board[move] = self.symbols[player]
        self.check_winner()
        
        # toggle turn
        self.turn = self.players[1] if player == self.players[0] else self.players[0]
