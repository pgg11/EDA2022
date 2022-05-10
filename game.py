#from random import randint
import board

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
        self.board = board.PawnBoard()


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


    #Falta aplicar lógica para decision de movimiento o colocación de pared
    def process_your_turn(self):

        #Actualiza el tablero
        self.board.updatePawnBoard(self.strBoard)
        #if randint(0, 4) == 0 and self.walls>0 :
        return self.board.processMove(self.side)
        #else:
        #   self.process_move(websocket)
    
#
#game = Game({"board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "walls": 10.0, "remaining_moves": 200.0, "player_1": "pablogg011@gmail.com", "side": "N", "score_1": 0.0, "score_2": 0.0, "player_2": "pabloTestBot", "turn_token": "0f1af4d0-3886-4bb3-9248-70f4a4394291", "game_id": "a00152f4-cfae-11ec-aef0-7ecdf393f9cc"})
#game.show_board()