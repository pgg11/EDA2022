from square import BoardSquare
from pawn import Pawn
from wall import Wall

class PawnBoard():
    
    def __init__(self,side):
        #Crea un tablero de 9x9 y en cada lugar de la matriz tiene un objeto BoardSquare
        self.board = [[BoardSquare(" ") for col in range(9)] for row in range(9)]
        self.side = side
        self.pawns = {}
        self.oppositePawns = {}
        self.lastPosition = [{'from_row': None, 'from_col': None},{'from_row': None, 'from_col': None}]

    def initBoard(self):
        #Agrega los peones a un diccionario con las posiciones iniciales
        if self.side=="N":
            self.pawns[0] = Pawn(0,1)
            self.oppositePawns[0] = Pawn(8,1)
            self.pawns[1] = Pawn(0,4)
            self.oppositePawns[1] = Pawn(8,4)
            self.pawns[2] = Pawn(0,7)
            self.oppositePawns[2] = Pawn(8,7)
        else:
            self.pawns[0] = Pawn(8,1)
            self.oppositePawns[0] = Pawn(0,1)
            self.pawns[1] = Pawn(8,4)
            self.oppositePawns[1] = Pawn(0,4)
            self.pawns[2] = Pawn(8,7)
            self.oppositePawns[2] = Pawn(0,7)
        #Marca los limites del tablero
        for row in range(9):
            for col in range(9):
                if row==0:
                    self.board[row][col].topBorder=False
                if row==8:
                    self.board[row][col].botBorder=False
                if col==0:
                    self.board[row][col].leftBorder=False
                if col==8:
                    self.board[row][col].rightBorder=False
                if row == 0:
                    if col == 1 or col == 4 or col == 7:
                        self.board[row][col].value = 'N'
                if row == 8:
                    if col == 1 or col == 4 or col == 7:
                        self.board[row][col].value = 'S'
    
    def positionPawns(self):
        #Escanea el tablero para dar las nuevas posiciones de los peones
        pawnCounter = 0
        oppositePawnCounter = 0
        for row in range(9):
            for col in range(9):
                if self.side == 'N':
                    if self.board[row][col].value == 'N':
                        self.pawns[pawnCounter].posY = row
                        self.pawns[pawnCounter].posX = col
                        pawnCounter += 1
                    if self.board[row][col].value == 'S':
                        self.oppositePawns[oppositePawnCounter].posY = row
                        self.oppositePawns[oppositePawnCounter].posX = col
                        oppositePawnCounter += 1

                else:
                    if self.board[row][col].value == 'S':
                        self.pawns[pawnCounter].posY = row
                        self.pawns[pawnCounter].posX = col
                        pawnCounter += 1
                    if self.board[row][col].value == 'N':
                        self.oppositePawns[oppositePawnCounter].posY = row
                        self.oppositePawns[oppositePawnCounter].posX = col
                        oppositePawnCounter += 1

    def updatePawnBoard(self,strBoard):
        #Con un puntero marca el caracter actual del string tablero
        boardPointer = 0
        for row in range(9):
            for col in range(9):
                if col < 8:
                    if strBoard[boardPointer+col*2+1] == '|': 
                        #Si encuentra una pared vertical marca los bordes afectados con False
                        self.board[row][col].rightBorder=False
                        self.board[row][col+1].leftBorder=False
                    else:
                        self.board[row][col].rightBorder=True
                        self.board[row][col+1].leftBorder=True
                if boardPointer < 272:
                    if strBoard[boardPointer+col*2+17] == '-':
                        #Si encuentra una pared horizontal marca los bordes afectados con False
                        self.board[row][col].botBorder=False
                        self.board[row+1][col].topBorder=False
                    else:
                        self.board[row][col].botBorder=True
                        self.board[row+1][col].topBorder=True
                        
                #Revisa si hay un peon en el cuadrado
                if strBoard[boardPointer+col*2]=="N":
                    self.board[row][col].value="N"
                elif  strBoard[boardPointer+col*2]=="S":
                    self.board[row][col].value="S"
                else:
                    self.board[row][col].value=" "
            #Sumo 34 al puntero para pasar a revisar la siguiente linea
            if row<8:
                boardPointer+=34
    
    def processMove(self):
        self.positionPawns()
        if self.side == 'N':
            move = Pawn.northMove(self.board,self.pawns,self.side,self.lastPosition)
            self.lastPosition.pop()
            self.lastPosition.insert(0,{'from_row':move['from_row'],'from_col':move['from_col']})
            return move
        else:
            move = Pawn.southMove(self.board,self.pawns,self.side,self.lastPosition)
            self.lastPosition.pop()
            self.lastPosition.insert(0,{'from_row':move['from_row'],'from_col':move['from_col']})
            return move
    
    def processWall(self):
        self.positionPawns()
        if self.side == 'N':
            return Wall.northSideWall(self.board,self.oppositePawns)
        else:
            return Wall.southSideWall(self.board,self.oppositePawns)