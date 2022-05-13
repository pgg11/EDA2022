

class Pawn():

    def __init__(self,row,col):
        self.posX = col
        self.posY = row
    
    def northMoveForward(board,pawns):
        for i in range(2,-1,-1):
            row = pawns[i].posY
            col = pawns[i].posX
            #Si no hay una pared en el lado sur del cuadrado chequeo posibles movimientos,
            #si la hay paso al siguiente peon
            if board[row][col].botBorder:
                #Si en la cuadrado siguiente hay un peon nuestro pasa al siguiente peon para mover
                if board[row+1][col].value == 'N':
                    if board[row][col+1].leftBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col+1})
                    if board[row][col-1].rightBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col-1})
                #Si en en el cuadrado siguiente hay un peon contrario y no esta en la fila
                #desde la que inicia, lo salta a menos que haya otra ficha o pared atras
                if board[row+1][col].value == 'S' and row<7:
                    if board[row+2][col].value == ' ' and board[row+1][col].botBorder:
                        return ({'from_row':row,'to_row':row+2,'from_col':col,'to_col':col})
                    continue
                #Si el peon está en el anteúltimo cuadrado y en el siguiente hay un peon contrario
                #pasa al siguiente peon para mover
                elif board[row+1][col].value == 'S' and row==7:
                    if board[row][col+1].leftBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col+1})
                    if board[row][col-1].rightBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col-1})
                #Si no se cumple ninguna de las condiciones anteriores y hay un cuadrado libre adelante
                #el peon avanza un casillero
                else:
                    return ({'from_row':row,'to_row':row+1,'from_col':col,'to_col':col})
            else:
                continue
    
    def southMoveForward(board,pawns):
        for i in range(3):
            row = pawns[i].posY
            col = pawns[i].posX
            #Si no hay una pared en el lado norte del cuadrado chequeo posibles movimientos,
            #si la hay paso al siguiente peon
            if board[row][col].topBorder:
                #Si en la cuadrado siguiente hay un peon nuestro pasa al siguiente peon para mover
                if board[row-1][col].value == 'S':
                    if board[row][col+1].leftBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col+1})
                    if board[row][col-1].rightBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col-1})
                #Si en en el cuadrado siguiente hay un peon contrario y no esta en la fila
                #desde la que inicia, lo salta a menos que haya otra ficha o pared atras
                if board[row-1][col].value == 'N' and row>1:
                    if board[row-2][col].value == ' ' and board[row-1][col].topBorder:
                        return ({'from_row':row,'to_row':row-2,'from_col':col,'to_col':col})
                    continue
                #Si el peon está en el anteúltimo cuadrado y en el siguiente hay un peon contrario
                #pasa al siguiente peon para mover
                elif board[row-1][col].value == 'N' and row==1:
                    if board[row][col+1].leftBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col+1})
                    if board[row][col-1].rightBorder:
                        return({'from_row':row,'to_row':row,'from_col':col,'to_col':col-1})
                #Si no se cumple ninguna de las condiciones anteriores y hay un cuadrado libre adelante
                #el peon avanza un casillero
                else:
                    return ({'from_row':row,'to_row':row-1,'from_col':col,'to_col':col})
            else:
                continue