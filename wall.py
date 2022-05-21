
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
    def northSideWall(cls,board,oppositePawns,walls):
        for i in range(3):
            row = oppositePawns[i].posY
            col = oppositePawns[i].posX
            if cls.isTrapped(row,col,board,'N'):
                continue 
            if walls == 10 or walls == 7 or walls == 4:
                if row < 3 or col < 1 or col > 7:
                    continue
                elif cls.checkWallPosition(row-3,col,'v',board):
                    return cls.wallPosition(row-3,col,'v')
            elif walls == 9 or walls == 6 or walls == 3:
                if row < 2 or col < 1 or col > 7:
                    continue
                elif cls.checkWallPosition(row-2,col-1,'v',board):
                    return cls.wallPosition(row-2,col-1,'v')
            elif walls == 8 or walls == 5 or walls == 2:
                if col > 7:
                    continue
                if cls.checkWallPosition(row-1,col,'h',board):
                    return cls.wallPosition(row-2,col,'h')
    
    @classmethod
    def southSideWall(cls,board,oppositePawns,walls):
        for i in range(2,-1,-1):
            row = oppositePawns[i].posY
            col = oppositePawns[i].posX
            if cls.isTrapped(row,col,board,'S'):
                continue   
            if walls == 10 or walls == 7 or walls == 4:
                if row > 5 or col < 1 or col > 7:
                    continue
                elif cls.checkWallPosition(row+2,col,'v',board):
                    return cls.wallPosition(row+2,col,'v')
            elif walls == 9 or walls == 6 or walls == 3:
                if row > 6 or col < 1 or col > 7:
                    continue
                elif cls.checkWallPosition(row+1,col-1,'v',board):
                    return cls.wallPosition(row+1,col-1,'v')
            elif walls == 8 or walls == 5 or walls == 2:
                if col > 7:
                    continue
                if cls.checkWallPosition(row+1,col,'h',board):
                    return cls.wallPosition(row+1,col,'h')