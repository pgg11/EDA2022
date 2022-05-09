

class Game():

    def __init__(self,data):
        self.side = data['side']
        self.score1 = data['score1']
        self.score2 = data['score2']
        self.player1 = data['player1']
        self.player2 = data['player2']
        self.remaining_moves = data['remaining_moves']
        self.walls = data['walls']
        self.board = data['board']
    
    def update_status(self,data):
        self.score1 = data['score1']
        self.score2 = data['score2']
        self.remaining_moves = data['remaining_moves']
        self.walls = data['walls']
        self.board = data['board']
    
    def show_board(self):
        index=0
        for symbol in range (len(self.board),symbol+17):
            print(self.board[index:index+17])
            index+=17

    def process_your_turn(self, websocket):
        pass