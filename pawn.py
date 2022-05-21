
class Pawn():

    def __init__(cls,row,col):
        cls.posX = col
        cls.posY = row
    
    @classmethod
    def northMove(cls,board,pawns,side,lastPosition):
        for i in range(2,-1,-1):
            row = pawns[i].posY
            col = pawns[i].posX
            #Si no hay una pared en el lado sur del cuadrado chequeo posibles movimientos
            if board[row][col].botBorder:
                #Si en el cuadrado siguiente hay un peon nuestro, si puede moverse a la derecha
                #lo hace, sino intenta a la izquierda, sino cambia de peon
                if board[row+1][col].value == 'N':
                    if cls.checkLeftSide(board,row,col,lastPosition):
                        return cls.moveToLeft(row,col)
                    if cls.checkRightSide(board,row,col,lastPosition):
                        return cls.moveToRight(row,col)
                    continue
                #Si en en el cuadrado siguiente hay un peon contrario y no esta en la fila
                #desde la que inicia, lo salta a menos que haya otro peón o pared atras
                elif board[row+1][col].value == 'S' and row<7:
                    #Salta peon contrario a menos que haya pared
                    if cls.checkJump(board,row,col,'N'):
                         return cls.jumpSouthPawn(row,col)

                    #Si hay pared detras del peon contrario busca saltos diagonales
                    if cls.checkLeftDiagonalJump(board,row,col,side):
                        return cls.leftDiagonalJump(row,col,side)
                    
                    if cls.checkRightDiagonalJump(board,row,col,'N'):
                        return cls.rightDiagonalJump(row,col,side)
                        
                    continue
                #Si el peon está en el anteúltimo cuadrado y en el siguiente hay un peon contrario
                #busca moverse a un costado
                elif board[row+1][col].value == 'S' and row==7:
                    if cls.checkLeftSide(board,row,col,lastPosition):
                        return cls.moveToLeft(row,col)
                    if cls.checkRightSide(board,row,col,lastPosition):
                        return cls.moveToRight(row,col)
                    continue
                #Si no se cumple ninguna de las condiciones anteriores y hay un cuadrado libre adelante
                #el peon avanza un casillero
                else:
                    return cls.moveForward(row,col,side)
            #Si el lado sur del cuadrado está bloqueado por una pared, se mueve a un costado
            if cls.checkLeftSide(board,row,col,lastPosition):
                return cls.moveToLeft(row,col)
            if cls.checkRightSide(board,row,col,lastPosition):
                return cls.moveToRight(row,col)
            continue      
    
    @classmethod
    def southMove(cls,board,pawns,side,lastPosition):
        for i in range(3):
            row = pawns[i].posY
            col = pawns[i].posX
            #Si no hay una pared en el lado norte del cuadrado chequeo posibles movimientos
            if board[row][col].topBorder:
                #Si en la cuadrado siguiente hay un peon nuestro, si puede moverse a la izquierda
                #lo hace, sino intenta a la derecha, sino cambia de peon
                if board[row-1][col].value == 'S':
                    if cls.checkRightSide(board,row,col,lastPosition):
                        return cls.moveToRight(row,col)
                    if cls.checkLeftSide(board,row,col,lastPosition):
                        return cls.moveToLeft(row,col)
                    continue
                #Si en en el cuadrado siguiente hay un peon contrario y no esta en la fila
                #desde la que inicia, lo salta a menos que haya otro peón o pared atras
                elif board[row-1][col].value == 'N' and row>1:
                    if cls.checkJump(board,row,col,side):
                        return cls.jumpNorthPawn(row,col)

                    #Si hay pared detras del peon contrario busca saltos diagonales
                    if cls.checkRightDiagonalJump(board,row,col,side):
                        return cls.rightDiagonalJump(row,col,side)

                    if cls.checkLeftDiagonalJump(board,row,col,side):
                        return cls.leftDiagonalJump(row,col,side)

                    continue
                #Si el peon está en el anteúltimo cuadrado y en el siguiente hay un peon contrario
                #busca moverse a un costado
                elif board[row-1][col].value == 'N' and row==1:
                    if cls.checkRightSide(board,row,col,lastPosition):
                        return cls.moveToRight(row,col)
                    if cls.checkLeftSide(board,row,col,lastPosition):
                        return cls.moveToLeft(row,col)
                    continue
                #Si no se cumple ninguna de las condiciones anteriores y hay un cuadrado libre adelante
                #el peon avanza un casillero
                else:
                    return cls.moveForward(row,col,side)
            #Si el lado norte del cuadrado está bloqueado, se mueve a un costado
            if cls.checkRightSide(board,row,col,lastPosition):
                return cls.moveToRight(row,col)
            if cls.checkLeftSide(board,row,col,lastPosition):
                return cls.moveToLeft(row,col)
            continue
            
    @classmethod
    def moveForward(cls,row,col,side):
        if side == 'N':
            return ({'from_row':row,'to_row':row+1,'from_col':col,'to_col':col})
        else:
            return ({'from_row':row,'to_row':row-1,'from_col':col,'to_col':col})
    
    @classmethod
    def moveBackwards(cls,row,col,side):
        if side == 'N':
            return ({'from_row':row,'to_row':row-1,'from_col':col,'to_col':col})
        else:
            return ({'from_row':row,'to_row':row+1,'from_col':col,'to_col':col})
    
    @classmethod
    def checkLeftSide(cls,board,row,col,lastPosition):
        if col > 0:
            return (board[row][col].leftBorder and board[row][col-1].value == ' ' and
              lastPosition != {'from_row':row,'from_col':col-1})
        else:
            return False
    
    @classmethod
    def checkRightSide(cls,board,row,col,lastPosition):
        if col < 8:
            return (board[row][col].rightBorder and board[row][col+1].value == ' ' and
              lastPosition != {'from_row':row,'from_col':col+1})
        else:
            return False

    @classmethod
    def moveToLeft(cls,row,col):
        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col-1})

    @classmethod
    def moveToRight(cls,row,col):
        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col+1})

    @classmethod
    def checkJump(cls,board,row,col,side):
        if side == 'N':
            return(board[row+2][col].value == ' ' and board[row+1][col].botBorder)
        else:
            return(board[row-2][col].value == ' ' and board[row-1][col].topBorder)

    @classmethod
    def jumpSouthPawn(cls,row,col):
        return ({'from_row':row,'to_row':row+2,'from_col':col,'to_col':col})
    
    @classmethod
    def jumpNorthPawn(cls,row,col):
        return ({'from_row':row,'to_row':row-2,'from_col':col,'to_col':col})
    
    @classmethod
    def checkRightDiagonalJump(cls,board,row,col,side):
        if side == 'N':
            if not board[row+1][col].botBorder:
                if col < 8:
                    return (board[row+1][col+1].leftBorder and board[row+1][col+1].value == ' ')
                else:
                    return False
        else:
            if not board[row-1][col].topBorder:
                if col < 8:
                    return (board[row-1][col+1].leftBorder and board[row-1][col+1].value == ' ')
                else:
                    return False

    @classmethod
    def checkLeftDiagonalJump(cls,board,row,col,side):
        if side == 'N':
            if not board[row+1][col].botBorder:
                if col > 0:
                    return(board[row+1][col-1].rightBorder and board[row+1][col-1].value == ' ')
                else:
                    return False
        else:
            if not board[row-1][col].topBorder:
                if col > 0:
                    return (board[row-1][col-1].rightBorder and board[row-1][col-1].value == ' ')
                else:
                    return False

    @classmethod
    def leftDiagonalJump(cls,row,col,side):
        if side == 'N':
            return ({'from_row':row,'to_row':row+1,'from_col':col,'to_col':col-1})
        else:
            return ({'from_row':row,'to_row':row-1,'from_col':col,'to_col':col-1})
    
    @classmethod
    def rightDiagonalJump(cls,row,col,side):
        if side == 'N':
            return ({'from_row':row,'to_row':row+1,'from_col':col,'to_col':col+1})
        else:
            return ({'from_row':row,'to_row':row-1,'from_col':col,'to_col':col+1})