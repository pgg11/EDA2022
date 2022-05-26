
class Wall():

    @classmethod
    def checkWallPosition(cls,row,col,orientation,board):
        if row<8 and col<8:
            if orientation == 'h':
                return ((board[row][col].botBorder and board[row][col+1].botBorder) and
                        (board[row][col].rightBorder or board[row+1][col].rightBorder))
            else:
                return ((board[row][col].rightBorder and board[row+1][col].rightBorder) and
                        (board[row][col].botBorder or board[row][col+1].botBorder))
        else:
            return False
    
    @classmethod
    def wallPosition(cls,row,col,orientation):
        if row<8 and col<8:
            return({'row':row,'col':col,'orientation':orientation})
        else:
            return('Invalid position')
    
    @classmethod
    def isTrapped(cls,row,col,board,side):
        if board[row][col].rightBorder == False and board[row][col].leftBorder == False:
            if side == 'N':
                return not board[row][col].topBorder or not board[row-1][col].topBorder
            else:
                return not board[row][col].botBorder or not board[row+1][col].botBorder
    
    #Busca encerrar en U a cualquier peon que avance de la fila de largada
    @classmethod
    def northSideWall(cls,board,oppositePawns):
        #Comienza por el peon más cerca de la meta que esté de la fila 7 hacia abajo
        for i in range(3):
            row = oppositePawns[i].posY
            col = oppositePawns[i].posX
            #Si ya está encerrado, continua con el siguiente más cerca de la meta
            if cls.isTrapped(row,col,board,'N'):
                continue
            if col<8 and row>3 and row < 8:
                #Verifica que no haya una pared en la derecha   
                if board[row-1][col].rightBorder and board[row-2][col].rightBorder:
                    #Verifica que se pueda poner la pared
                    if cls.checkWallPosition(row-3,col,'v',board):
                        return cls.wallPosition(row-3,col,'v')
                    if not board[row-1][col].leftBorder and not board[row-2][col].leftBorder:
                        if cls.checkWallPosition(row-2,col,'v',board):
                            return cls.wallPosition(row-2,col,'v')
            if col>0 and row>2 and row<8:
                #Si habia pared en la derecha, se fija que no haya pared en la izquierda
                if board[row-1][col].leftBorder and board[row-2][col].leftBorder:         
                    #Chequea que se pueda poner la pared izquierda
                    if not board[row-2][col].rightBorder and not board[row-1][col].rightBorder:
                        if cls.checkWallPosition(row-2,col-1,'v',board):
                            return cls.wallPosition(row-2,col-1,'v')
            if row>1:
                #Si ya hay pared en en ambos lados busca la altura para poner la pared horizontal
                #para terminar el encierro
                if not board[row-1][col].rightBorder and not board[row-1][col].leftBorder:
                    if not board[row-2][col].rightBorder and not board[row-2][col].leftBorder:
                        if cls.checkWallPosition(row-3,col,'h',board):
                            return cls.wallPosition(row-3,col,'h')
                        elif cls.checkWallPosition(row-3,col-1,'h',board):
                            return cls.wallPosition(row-3,col-1,'h')
                    if not board[row][col].rightBorder and not board[row][col].leftBorder:
                        if cls.checkWallPosition(row-2,col,'h',board):
                            return cls.wallPosition(row-2,col,'h')
                        elif cls.checkWallPosition(row-2,col-1,'h',board):
                            return cls.wallPosition(row-2,col-1,'h')
                 
    
    #Busca encerrar en U a cualquier peon que avance de la fila de largada
    @classmethod
    def southSideWall(cls,board,oppositePawns):
        #Comienza por el peon más cerca de la meta
        for i in range(2,-1,-1):
            row = oppositePawns[i].posY
            col = oppositePawns[i].posX
            #Si ya está encerrado, continua con el siguiente más cerca de la meta
            if cls.isTrapped(row,col,board,'S'):
                continue
            if row > 0 and row < 6 and col < 8:
                if row < 5:
                    #Verifica que no haya una pared en la derecha   
                    if board[row+1][col].rightBorder and board[row+2][col].rightBorder:
                        #Verifica que se pueda poner la pared
                        if cls.checkWallPosition(row+2,col,'v',board):
                            return cls.wallPosition(row+2,col,'v')
                if board[row][col].rightBorder and board[row+1][col].rightBorder:
                    if cls.checkWallPosition(row+1,col,'v',board):
                        return cls.wallPosition(row+1,col,'v')
            if row < 6 and row > 1 and col > 0:
                #Si habia pared en la derecha, se fija que no haya pared en la izquierda
                if board[row+1][col].leftBorder and board[row+2][col].leftBorder:
                    #Chequea que se pueda poner la pared izquierda
                    if not board[row+2][col].rightBorder and not board[row+1][col].rightBorder:
                        if cls.checkWallPosition(row+1,col-1,'v',board):
                            return cls.wallPosition(row+1,col-1,'v')
            if row < 8:
                #Si ya hay pared en en ambos lados busca la altura para poner la pared horizontal
                #para terminar el encierro
                if not board[row+1][col].rightBorder and not board[row+1][col].leftBorder:
                    if not board[row+2][col].leftBorder and not board[row+2][col].rightBorder:
                        if cls.checkWallPosition(row+2,col-1,'h',board):
                            return cls.wallPosition(row+2,col-1,'h')
                        elif cls.checkWallPosition(row+2,col,'h',board):
                            return cls.wallPosition(row+2,col,'h')
                    if not board[row][col].leftBorder and not board[row][col].rightBorder:
                        if cls.checkWallPosition(row+1,col-1,'h',board):
                            return cls.wallPosition(row+1,col-1,'h')
                        elif cls.checkWallPosition(row+1,col,'h',board):
                            return cls.wallPosition(row+1,col,'h')