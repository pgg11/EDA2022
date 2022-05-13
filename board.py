import square
import pawn

class PawnBoard():
    
    def __init__(self,side):
        self.board = [[square.BoardSquare("") for col in range(9)] for row in range(9)]
        self.side = side
        self.pawns = {}


    
    #Marca los bordes del tablero como lados bloqueados
    def markBorders(self):
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
    
    def positionPawns(self):
        #Si no tengo ubicados los peones, los agrego a un diccionario con las posiciones iniciales
        if len(self.pawns) == 0:
            self.markBorders()
            if self.side=="N":
                self.pawns[0] = pawn.Pawn(0,1)
                self.pawns[1] = pawn.Pawn(0,4)
                self.pawns[2] = pawn.Pawn(0,7)
            else:
                self.pawns[0] = pawn.Pawn(8,1)
                self.pawns[1] = pawn.Pawn(8,4)
                self.pawns[2] = pawn.Pawn(8,7)
        else:
            pawnCounter = 0
            for row in range(9):
                for col in range(9):
                    if self.side == 'N':
                        if self.board[row][col].value == 'N':
                            self.pawns[pawnCounter].posY = row
                            self.pawns[pawnCounter].posX = col
                            pawnCounter += 1
                    else:
                        if self.board[row][col].value == 'S':
                            self.pawns[pawnCounter].posY = row
                            self.pawns[pawnCounter].posX = col
                            pawnCounter += 1

    def updatePawnBoard(self,strBoard):
        #Con un puntero marco el caracter strBoard para buscar paredes
        boardPointer = 0
        for row in range(9):
            #Aisla fila del tablero en cada iteracion
            string_row=strBoard[17*(row*2): 17*(row*2) + 17]
            for col in range(9):
                if strBoard[boardPointer+col+1] == '|' and col < 8:
                    #Si encuentra una pared vertical marca los bordes afectados con False
                    self.board[row][col-1].rightBorder=False
                    self.board[row][col+1].leftBorder=False
                if strBoard[boardPointer+col+9] == '-' and col < 8:
                    #Si encuentra una pared horizontal marca los bordes afectados con False
                        self.board[row][col].botBorder=False
                        self.board[row+1][col].topBorder=False
                #Revisa si hay un peon en el cuadrado
                if string_row[col*2]=="N":
                    self.board[row][col]=square.BoardSquare("N")
                elif  string_row[col*2]=="S":
                    self.board[row][col]=square.BoardSquare("S")
                else:
                    self.board[row][col]=square.BoardSquare(" ")
            #Sumo 17 al puntero para pasar a la siguiente linea
            if row<7:
                boardPointer+=34
    
    def printPawnBoard(self):
        for row in range(9):
            for col in range(9):
                print(self.board[row][col].value,end='')
            print()
    
    #Falta aplicar lógica de movimiento de peones
    def processMove(self):
        self.positionPawns()
        if self.side == 'N':
            return pawn.Pawn.northMoveForward(self.board,self.pawns)
        else:
            return pawn.Pawn.southMoveForward(self.board,self.pawns)