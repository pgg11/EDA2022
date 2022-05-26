import unittest
from pawn import Pawn
from board import PawnBoard

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.northBoard = PawnBoard('N')
        self.southBoard = PawnBoard('S')

    def test_checkForward(self):
        #Como se guardan las últimas dos posiciones de los peones y las primeras dos
        #son None, quito la última
        self.northBoard.lastPosition.pop()
        #Inserto en la posicion 1 la última posicion del peon
        self.northBoard.lastPosition.insert(1,{'from_row':3,'from_col':2})
        #Verifico que el peon no avance a una posicion en la que estuvo anteriormente
        self.assertFalse(Pawn.checkForward(2,2,'N',self.northBoard.lastPosition))
        #Quito la última posición del peon
        self.northBoard.lastPosition.pop()
        #Verifico que esta vez se pueda mover a la posición siguiente
        self.assertTrue(Pawn.checkForward(2,2,'N',self.northBoard.lastPosition))

        #Repite el procedimiento anterior pero en un tablero del lado sur
        self.southBoard.lastPosition.pop()
        self.southBoard.lastPosition.insert(1,{'from_row':2,'from_col':7})
        self.assertFalse(Pawn.checkForward(3,7,'S',self.southBoard.lastPosition))
        self.southBoard.lastPosition.pop()
        self.assertTrue(Pawn.checkForward(3,7,'S',self.northBoard.lastPosition))

    def test_moveForward(self):
        #Verifica que los peones del lado norte avancen correctamente
        self.assertEqual(Pawn.moveForward(0,0,'N'),{'from_row':0,'from_col':0,'to_row':1,'to_col':0})
        self.assertEqual(Pawn.moveForward(7,8,'N'),{'from_row':7,'from_col':8,'to_row':8,'to_col':8})
        self.assertEqual(Pawn.moveForward(4,4,'N'),{'from_row':4,'from_col':4,'to_row':5,'to_col':4})
        #Verifica que los peones del lado sur avancen correctamente
        self.assertEqual(Pawn.moveForward(8,1,'S'),{'from_row':8,'from_col':1,'to_row':7,'to_col':1})
        self.assertEqual(Pawn.moveForward(1,3,'S'),{'from_row':1,'from_col':3,'to_row':0,'to_col':3})
        self.assertEqual(Pawn.moveForward(4,8,'S'),{'from_row':4,'from_col':8,'to_row':3,'to_col':8})

    def test_checkLeftSide(self):

        #Inicializo el tablero del lado norte
        self.northBoard.initBoard()
        #Se agregan peones N en distintos lugares para verificar que el chequeo funcione correctamente
        self.northBoard.board[4][4].value = 'N'
        #Agrega un bloqueo en el borde izquiero de la posición 4,4 
        self.northBoard.board[4][4].leftBorder = False
        self.northBoard.board[6][3].value = 'N'
        self.northBoard.board[6][2].value = 'N'
        self.northBoard.board[2][0].value = 'N'

        #Verifica que de la posicion inicial 0,1 se pueda mover a la izquierda
        self.assertTrue(Pawn.checkLeftSide(self.northBoard.board,0,1,self.northBoard.lastPosition))

        #Agrega una ultima posicion del peon desde la posicion 0,6
        self.northBoard.lastPosition.pop()
        self.northBoard.lastPosition.insert(0,{'from_row': 0, 'from_col': 6})
        #Verifica que el peon ubicado en 0,7 no se pueda mover a la izquierda
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,0,7,self.northBoard.lastPosition))
        #Verifica que el peon que tiene una pared en la izquierda no pueda moverse hacia ese lado
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,4,4,self.northBoard.lastPosition))
        #Verifica que el peón que tiene un peón del mismo bando a su izquierda no pueda moverse hacia ese lado
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,6,3,self.northBoard.lastPosition))
        #Verifica que un peon no pueda salirse de los limites del tablero del lado izquiero
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,2,0,self.northBoard.lastPosition))
    
    def test_checkRightSide(self):

        #Inicializa el tablero del lado sur
        self.southBoard.initBoard()
        #Agrega peones del lado sur en distintos luagres del tablero
        self.southBoard.board[4][4].value = 'S'
        #Marca un bloqueo en la derecha del casillero 4,4
        self.southBoard.board[4][4].rightBorder = False
        self.southBoard.board[6][3].value = 'S'
        self.southBoard.board[6][2].value = 'S'
        self.southBoard.board[2][8].value = 'S'

        #Verifica que el peon ubicado en la posición 8,1 se pueda mover a la derecha
        self.assertTrue(Pawn.checkRightSide(self.southBoard.board,8,1,self.southBoard.lastPosition))
        #Agrega a las ultimas posiciones, la posición 8,8
        self.southBoard.lastPosition.pop()
        self.southBoard.lastPosition.insert(0,{'from_row': 8, 'from_col': 8})
        #Verfica que el peon ubicado en la posicion 8,7, no se pueda mover a la derecha
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,8,7,self.southBoard.lastPosition))
        #Verifica que el peon ubicado en 4,4 no pueda moverse a la derecha, ya que está bloqueado
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,4,4,self.southBoard.lastPosition))
        #Verifica que el peón que tiene un peón del mismo bando a su derecha no pueda moverse hacia ese lado
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,6,2,self.southBoard.lastPosition))
        #Verifica que un peon no pueda salirse de los limites del tablero del lado derecho
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,2,8,self.southBoard.lastPosition))
    
    def test_checkJump(self):
        
        #Inicializa el tablero del lado norte y coloca peones en distintos casilleros
        self.northBoard.initBoard()
        self.northBoard.board[1][1].value = 'S'
        self.northBoard.board[1][7].value = 'S'
        self.northBoard.board[1][7].botBorder = False
        self.northBoard.board[6][5].value = 'N'
        self.northBoard.board[7][5].value = 'S'

        #Verifica que un peon del lado norte pueda saltar a un peón contrario
        self.assertTrue(Pawn.checkJump(self.northBoard.board,0,1,self.northBoard.side))
        #Verifica que si hay una pared detras del peon contrario, no lo pueda saltar
        self.assertFalse(Pawn.checkJump(self.northBoard.board,0,7,self.northBoard.side))
        #Verifica que un peon pueda saltar a uno contrario cuando se ubica en la anteultima fila
        self.assertTrue(Pawn.checkJump(self.northBoard.board,6,5,self.northBoard.side))        
        
        self.southBoard.initBoard()
        self.southBoard.board[7][1].value = 'N'
        self.southBoard.board[7][7].value = 'N'
        self.southBoard.board[7][7].topBorder = False
        self.southBoard.board[2][6].value = 'N'
        self.southBoard.board[3][6].value = 'S'

        #Verifica que un peon del lado sur pueda saltar a un peón contrario
        self.assertTrue(Pawn.checkJump(self.southBoard.board,8,1,self.southBoard.side))
        #Verifica que si hay una pared detras del peon contrario, no lo pueda saltar
        self.assertFalse(Pawn.checkJump(self.southBoard.board,8,7,self.southBoard.side))
        #Verifica que un peon pueda saltar a uno contrario cuando se ubica en la anteultima fila
        self.assertTrue(Pawn.checkJump(self.southBoard.board,3,6,self.southBoard.side))
    
    def test_checkRightDiagonalJump(self):

        #Inicia el tablero del lado norte y coloca peones para los casos de prueba
        self.northBoard.initBoard()
        self.northBoard.board[2][3].value = 'N'
        self.northBoard.board[3][3].value = 'S'
        self.northBoard.board[3][3].botBorder = False
        self.northBoard.board[4][4].value = 'N'
        self.northBoard.board[5][4].value = 'S'
        self.northBoard.board[5][4].botBorder = False
        self.northBoard.board[5][5].leftBorder = False

        #Verifica que se pueda hacer un salto diagonal derecho desde el lado norte si hay un peon contrario
        #enfrente con una pared detras, y no hay una pared vertical que lo imposibilite
        self.assertTrue(Pawn.checkRightDiagonalJump(self.northBoard.board,2,3,self.northBoard.side))
        #Verifica que si hay una pared vertical en la fila que sigue, no pueda hacer el salto diagonal
        self.assertFalse(Pawn.checkRightDiagonalJump(self.northBoard.board,4,4,self.northBoard.side))       
        
        #Inicia el tablero del lado sur y coloca peones para los casos de prueba
        self.southBoard.initBoard()
        self.southBoard.board[7][1].value = 'N'
        self.southBoard.board[7][1].topBorder = False
        self.southBoard.board[4][4].value = 'N'
        self.southBoard.board[5][4].value = 'S'
        self.southBoard.board[4][4].topBorder = False
        self.southBoard.board[4][5].leftBorder = False

        #Verifica que se pueda hacer un salto diagonal derecho desde el lado sur si hay un peon contrario
        #enfrente con una pared detras, y no hay una pared vertical que lo imposibilite
        self.assertTrue(Pawn.checkRightDiagonalJump(self.southBoard.board,8,1,self.southBoard.side))
        #Verifica que si hay una pared vertical en la fila que sigue, no pueda hacer el salto diagonal
        self.assertFalse(Pawn.checkRightDiagonalJump(self.southBoard.board,5,4,self.southBoard.side))

    def test_checkLeftDiagonalJump(self):
        #Verifica lo mismo que el caso anterior, pero para saltos diagonales izquierdos
        
        self.northBoard.initBoard()
        self.northBoard.board[1][4].value = 'S'
        self.northBoard.board[1][4].botBorder = False
        self.northBoard.board[6][5].value = 'N'
        self.northBoard.board[7][5].value = 'S'
        self.northBoard.board[7][5].botBorder = False
        self.northBoard.board[7][4].rightBorder = False

        self.assertTrue(Pawn.checkLeftDiagonalJump(self.northBoard.board,0,4,self.northBoard.side))
        self.assertFalse(Pawn.checkLeftDiagonalJump(self.northBoard.board,6,5,self.northBoard.side))       
        
        self.southBoard.initBoard()
        self.southBoard.board[7][4].value = 'N'
        self.southBoard.board[7][4].topBorder = False
        self.southBoard.board[4][4].value = 'N'
        self.southBoard.board[5][4].value = 'S'
        self.southBoard.board[4][4].topBorder = False
        self.southBoard.board[4][3].rightBorder = False

        self.assertTrue(Pawn.checkLeftDiagonalJump(self.southBoard.board,8,4,self.southBoard.side))
        self.assertFalse(Pawn.checkLeftDiagonalJump(self.southBoard.board,5,4,self.southBoard.side))

    def test_moveToLeft(self):

        #Verifica que los movimientos a la izquierda se hagan correctamente
        self.assertEqual(Pawn.moveToLeft(0,1),{'from_row':0,'from_col':1,'to_row':0,'to_col':0})
        self.assertEqual(Pawn.moveToLeft(0,8),{'from_row':0,'from_col':8,'to_row':0,'to_col':7})
        self.assertEqual(Pawn.moveToLeft(4,4),{'from_row':4,'from_col':4,'to_row':4,'to_col':3})
        self.assertEqual(Pawn.moveToLeft(8,1),{'from_row':8,'from_col':1,'to_row':8,'to_col':0})
        self.assertEqual(Pawn.moveToLeft(8,8),{'from_row':8,'from_col':8,'to_row':8,'to_col':7})
        self.assertEqual(Pawn.moveToLeft(2,2),{'from_row':2,'from_col':2,'to_row':2,'to_col':1})
    
    def test_moveToRight(self):
        #Verifica que los movimientos a la derecha se hagan correctamente
        self.assertEqual(Pawn.moveToRight(0,1),{'from_row':0,'from_col':1,'to_row':0,'to_col':2})
        self.assertEqual(Pawn.moveToRight(0,7),{'from_row':0,'from_col':7,'to_row':0,'to_col':8})
        self.assertEqual(Pawn.moveToRight(4,4),{'from_row':4,'from_col':4,'to_row':4,'to_col':5})
        self.assertEqual(Pawn.moveToRight(8,1),{'from_row':8,'from_col':1,'to_row':8,'to_col':2})
        self.assertEqual(Pawn.moveToRight(8,0),{'from_row':8,'from_col':0,'to_row':8,'to_col':1})
        self.assertEqual(Pawn.moveToRight(2,2),{'from_row':2,'from_col':2,'to_row':2,'to_col':3})
    
    def test_jumpSouthPawn(self):
        #Verifica que los saltos del lado sur se hagan correctamente
        self.assertEqual(Pawn.jumpSouthPawn(0,1),{'from_row':0,'from_col':1,'to_row':2,'to_col':1})
        self.assertEqual(Pawn.jumpSouthPawn(0,8),{'from_row':0,'from_col':8,'to_row':2,'to_col':8})
        self.assertEqual(Pawn.jumpSouthPawn(4,4),{'from_row':4,'from_col':4,'to_row':6,'to_col':4})
        self.assertEqual(Pawn.jumpSouthPawn(6,8),{'from_row':6,'from_col':8,'to_row':8,'to_col':8})
        self.assertEqual(Pawn.jumpSouthPawn(6,0),{'from_row':6,'from_col':0,'to_row':8,'to_col':0})
        self.assertEqual(Pawn.jumpSouthPawn(4,5),{'from_row':4,'from_col':5,'to_row':6,'to_col':5})
    
    def test_jumpNorthPawn(self):
        #Verifica que los saltos del lado norte se hagan correctamente
        self.assertEqual(Pawn.jumpNorthPawn(2,1),{'from_row':2,'from_col':1,'to_row':0,'to_col':1})
        self.assertEqual(Pawn.jumpNorthPawn(2,8),{'from_row':2,'from_col':8,'to_row':0,'to_col':8})
        self.assertEqual(Pawn.jumpNorthPawn(4,4),{'from_row':4,'from_col':4,'to_row':2,'to_col':4})
        self.assertEqual(Pawn.jumpNorthPawn(5,8),{'from_row':5,'from_col':8,'to_row':3,'to_col':8})
        self.assertEqual(Pawn.jumpNorthPawn(6,0),{'from_row':6,'from_col':0,'to_row':4,'to_col':0})
        self.assertEqual(Pawn.jumpNorthPawn(4,5),{'from_row':4,'from_col':5,'to_row':2,'to_col':5})
    
    def test_leftDiagonalJump(self):
        #Verifica que los saltos diagonales izquierdos del lado norte se hagan correctamente
        self.assertEqual(Pawn.leftDiagonalJump(0,8,'N'),{'from_row':0,'from_col':8,'to_row':1,'to_col':7})
        self.assertEqual(Pawn.leftDiagonalJump(3,3,'N'),{'from_row':3,'from_col':3,'to_row':4,'to_col':2})
        self.assertEqual(Pawn.leftDiagonalJump(6,8,'N'),{'from_row':6,'from_col':8,'to_row':7,'to_col':7})
        #Verifica que los saltos diagonales izquierdos del lado sur se hagan correctamente
        self.assertEqual(Pawn.leftDiagonalJump(3,1,'S'),{'from_row':3,'from_col':1,'to_row':2,'to_col':0})
        self.assertEqual(Pawn.leftDiagonalJump(4,4,'S'),{'from_row':4,'from_col':4,'to_row':3,'to_col':3})
        self.assertEqual(Pawn.leftDiagonalJump(8,8,'S'),{'from_row':8,'from_col':8,'to_row':7,'to_col':7})
    
    def test_rightDiagonalJump(self):
        #Verifica que los saltos diagonales derechos del lado norte se hagan correctamente
        self.assertEqual(Pawn.rightDiagonalJump(0,0,'N'),{'from_row':0,'from_col':0,'to_row':1,'to_col':1})
        self.assertEqual(Pawn.rightDiagonalJump(3,3,'N'),{'from_row':3,'from_col':3,'to_row':4,'to_col':4})
        self.assertEqual(Pawn.rightDiagonalJump(6,7,'N'),{'from_row':6,'from_col':7,'to_row':7,'to_col':8})
        #Verifica que los saltos diagonales derechos del lado sur se hagan correctamente
        self.assertEqual(Pawn.rightDiagonalJump(3,7,'S'),{'from_row':3,'from_col':7,'to_row':2,'to_col':8})
        self.assertEqual(Pawn.rightDiagonalJump(4,4,'S'),{'from_row':4,'from_col':4,'to_row':3,'to_col':5})
        self.assertEqual(Pawn.rightDiagonalJump(8,0,'S'),{'from_row':8,'from_col':0,'to_row':7,'to_col':1})


if __name__ == '__main__':
    unittest.main()