
import square

class PawnBoard():
    
    def __init__(self):
        self.board = [[square.BoardSquare(row,col,"") for col in range(9)] for row in range(9)]
    
    def updatePawnBoard(self,strBoard):
        for row in range(9):
            string_row=strBoard[17*(row*2): 17*(row*2) + 17]
            for col in range(9):
                if string_row[col*2]=="N":
                    self.board[row][col]=square.BoardSquare(row,col,"N")
                elif  string_row[col*2]=="S":
                    self.board[row][col]=square.BoardSquare(row,col,"S")
                else:
                    self.board[row][col]=square.BoardSquare(row,col," ")
    
    def printPawnBoard(self):
        for row in range(9):
            for col in range(9):
                print(self.board[row][col].value,end='')
            print()
    
    #Falta aplicar lógica de movimiento de peones
    def processMove(self,side):
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value == side:
                    print(self.board[row][col].value)
                    if side == "N":
                        return ({"from_row":row, "to_row":row+1, "from_col":col, "to_col":col })
                    if side == "S":
                        return ({"from_row":row, "to_row":row-1, "from_col":col, "to_col":col })
