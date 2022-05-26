from board import PawnBoard

class Game():

    def __init__(self,data):
        self.side = data["side"]
        self.score1 = data["score_1"]
        self.score2 = data["score_2"]
        self.player1 = data["player_1"]
        self.player2 = data["player_2"]
        self.remaining_moves = data["remaining_moves"]
        self.walls = data["walls"]
        self.strBoard = data["board"]
        self.board = PawnBoard(data["side"])
        self.board.initBoard()


    def update_status(self,data):
        self.score1 = data["score_1"]
        self.score2 = data["score_2"]
        self.remaining_moves = data["remaining_moves"]
        self.walls = data["walls"]
        self.strBoard = data["board"]
    
    def show_board(self):
        print(f"Side: {self.side}")
        print(f"Player 1: {self.player1}    |   Player 2: {self.player2}")
        print(f"Score 1: {self.score1}      |   Score 2: {self.score2}")
        line_names="0a1b2c3d4e5f6g7h8"
        #Board
        print("  " + line_names)
        print("  -----------------")
        for row in range(17):
            print(line_names[row]+"|",end='')
            print(self.strBoard[17*(row):17*(row) + 17],end='\n')
    
    def process_your_turn(self):

        #Actualiza el tablero antes de cada jugada
        self.board.updatePawnBoard(self.strBoard)
        if self.walls>1 and self.board.processWall() != None:
            return self.board.processWall()
        else:
            return self.board.processMove()