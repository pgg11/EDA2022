
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
    
    @classmethod
    def northSideWall(cls,board,oppositePawns):
        #Comienza por el peon más cerca de la meta
        for i in range(3):
            row = oppositePawns[i].posY
            col = oppositePawns[i].posX
            #Si ya está encerrado, continua con el siguiente más cerca de la meta
            if cls.isTrapped(row,col,board,'N'):
                continue 
            #Verifica que no haya una pared en la derecha   
            if board[row-1][col].rightBorder and board[row-2][col].rightBorder:
                if row < 3 or col < 1 or col > 7:
                    continue
                #Verifica que se pueda poner la pared
                elif cls.checkWallPosition(row-3,col,'v',board):
                    return cls.wallPosition(row-3,col,'v')
            #Si habia pared en la derecha, se fija que no haya pared en la izquierda
            elif board[row-1][col].leftBorder and board[row-2][col].leftBorder:
                if row < 3 or col < 1 or col > 7:
                    continue
                #verifica en que altura está la pared de la derecha para ponerla en la misma altura
                elif not board[row-2][col].rightBorder and not board[row-3][col].rightBorder:
                    if cls.checkWallPosition(row-2,col-1,'v',board):
                        return cls.wallPosition(row-3,col-1,'v')
                elif not board[row-2][col].rightBorder and not board[row-1][col].rightBorder:
                    if cls.checkWallPosition(row-2,col-1,'v',board):
                        return cls.wallPosition(row-2,col-1,'v')
            #Si ya hay pared en en ambos lados busca la altura para poner la pared horizontal
            #para terminar el encierro
            elif board[row-1][col].topBorder:
                if col > 7 or row < 3:
                    continue
                elif not board[row-2][col].leftBorder and not board[row-3][col].leftBorder:
                    if cls.checkWallPosition(row-4,col,'h',board):
                        return cls.wallPosition(row-4,col,'h')
                elif not board[row-1][col].leftBorder and not board[row-2][col].leftBorder:
                    if cls.checkWallPosition(row-3,col,'h',board):
                        return cls.wallPosition(row-3,col,'h')
                elif not board[row-1][col].leftBorder and not board[row][col].leftBorder:
                    if cls.checkWallPosition(row-2,col,'h',board):
                        return cls.wallPosition(row-2,col,'h')
    
    @classmethod
    def southSideWall(cls,board,oppositePawns):
        #Comienza por el peon más cerca de la meta
        for i in range(2,-1,-1):
            row = oppositePawns[i].posY
            col = oppositePawns[i].posX
            #Si ya está encerrado, continua con el siguiente más cerca de la meta
            if cls.isTrapped(row,col,board,'S'):
                continue
            #Verifica que no haya una pared en la derecha   
            if board[row+2][col].rightBorder and board[row+1][col].rightBorder:
                if row > 5 or col < 1 or col > 7:
                    continue
                #Verifica que se pueda poner la pared
                elif cls.checkWallPosition(row+2,col,'v',board):
                    return cls.wallPosition(row+2,col,'v')
            #Si habia pared en la derecha, se fija que no haya pared en la izquierda
            elif board[row+1][col].leftBorder and board[row+2][col].leftBorder:
                if row > 6 or col < 1 or col > 7:
                    continue
                #verifica en que altura está la pared de la derecha para ponerla en la misma altura
                elif not board[row+2][col].rightBorder and not board[row+3][col].rightBorder:
                    if cls.checkWallPosition(row+2,col-1,'v',board):
                        return cls.wallPosition(row+2,col-1,'v')
                elif not board[row+2][col].rightBorder and not board[row+1][col].rightBorder:
                    if cls.checkWallPosition(row+2,col-1,'v',board):
                        return cls.wallPosition(row+1,col-1,'v')
            #Si ya hay pared en en ambos lados busca la altura para poner la pared horizontal
            #para terminar el encierro
            elif board[row+1][col].botBorder:
                if col > 7:
                    continue
                elif not board[row+2][col].leftBorder and not board[row+3][col].leftBorder:
                    if cls.checkWallPosition(row+3,col,'h',board):
                        return cls.wallPosition(row+3,col,'h')
                elif not board[row+1][col].leftBorder and not board[row+2][col].leftBorder:
                    if cls.checkWallPosition(row+2,col,'h',board):
                        return cls.wallPosition(row+2,col,'h')
                elif not board[row+1][col].leftBorder and not board[row][col].leftBorder:
                    if cls.checkWallPosition(row+1,col,'h',board):
                        return cls.wallPosition(row+1,col,'h')