from random import randint
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

        line_names="0a1b2c3d4e5f6g7h8"
        #Board
        print("  " + line_names)
        print("  -----------------")
        for row in range(17):
            print(line_names[row]+"|",end='')
            print(self.strBoard[17*(row):17*(row) + 17],end='\n')

    #En caso de error revisar desde acá
    #Falta terminar lógica para decision de movimiento o colocación de pared
    def process_your_turn(self):

        #Actualiza el tablero
        self.board.updatePawnBoard(self.strBoard)
        if randint(0, 9) == 0 and self.walls>0 :
            return self.board.processWall()
        else:
            return self.board.processMove()