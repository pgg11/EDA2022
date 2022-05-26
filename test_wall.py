import unittest
from wall import Wall
from board import PawnBoard


class TestWall(unittest.TestCase):

    def setUp(self):
        self.board = PawnBoard('N').board
        self.northBoard = PawnBoard('N')
        self.southBoard = PawnBoard('S')

    def test_checkWallPosition(self):
        
        #Verifica que si no se pueda poner pared vertical en la fila 8
        self.assertFalse(Wall.checkWallPosition(8,5,'v',self.board))
        #Verifica que si no se pueda poner pared horizontal en la columna 8
        self.assertFalse(Wall.checkWallPosition(4,8,'h',self.board))
        #Verifica que si no se pueda poner pared vertical en la columna 8
        self.assertFalse(Wall.checkWallPosition(0,8,'v',self.board))
        #Verifica que si no se pueda poner pared horizontal en la fila 8
        self.assertFalse(Wall.checkWallPosition(8,3,'h',self.board))

        #Marca bordes inferiores de los casilleros 4,4 y 4,5 como bloqueados
        self.board[4][4].botBorder = False
        self.board[4][5].botBorder = False
        #Verifica que no se pueda poner una pared vertical entre ellos
        self.assertFalse(Wall.checkWallPosition(4,4,'v',self.board))
        #Marca bordes derechos de los casilleros 2,6 y 3,6 como bloqueados
        self.board[2][6].rightBorder = False
        self.board[3][6].rightBorder = False
        #Verifica que no se pueda poner una pared horizontal entre ellos
        self.assertFalse(Wall.checkWallPosition(2,6,'h',self.board))
        
        #Verifica que se puedan poner paredes horizontales y verticales en lugares permitidos
        self.assertTrue(Wall.checkWallPosition(0,2,'h',self.board))
        self.assertTrue(Wall.checkWallPosition(0,0,'v',self.board))
        self.assertTrue(Wall.checkWallPosition(4,3,'v',self.board))
        self.assertTrue(Wall.checkWallPosition(4,6,'v',self.board))
        self.assertTrue(Wall.checkWallPosition(1,6,'h',self.board))
        self.assertTrue(Wall.checkWallPosition(7,7,'h',self.board))
        self.assertTrue(Wall.checkWallPosition(7,3,'v',self.board))
    
    def test_wallPosition(self):
        #Verifico que se envia correctamente la posición y orientación de las paredes
        self.assertEqual(Wall.wallPosition(2,5,'v'),{'row':2,'col':5,'orientation':'v'})
        self.assertEqual(Wall.wallPosition(7,7,'v'),{'row':7,'col':7,'orientation':'v'})
        self.assertEqual(Wall.wallPosition(0,0,'v'),{'row':0,'col':0,'orientation':'v'})
        self.assertEqual(Wall.wallPosition(4,7,'h'),{'row':4,'col':7,'orientation':'h'})
        self.assertEqual(Wall.wallPosition(0,7,'h'),{'row':0,'col':7,'orientation':'h'})
        self.assertEqual(Wall.wallPosition(7,0,'h'),{'row':7,'col':0,'orientation':'h'})
        #Verifica que si no es una posicion valida recibe un mensaje de 'Invalid position'
        self.assertEqual(Wall.wallPosition(8,3,'v'),'Invalid position')
        self.assertEqual(Wall.wallPosition(0,8,'v'),'Invalid position')
        self.assertEqual(Wall.wallPosition(8,8,'h'),'Invalid position')
        self.assertEqual(Wall.wallPosition(8,6,'h'),'Invalid position')
    
    def test_isTrapped(self):

        #Inicia el tablero del lado norte
        self.northBoard.initBoard()
        #Mueve el peon de la posicion 8,1 a la posicion 5,1
        self.northBoard.board[8][1].value = ' '
        self.northBoard.board[5][1].value = 'S'
        #Actualiza las posiciones de los peones
        self.northBoard.positionPawns()
        #Marca los bordes alrededor del peon en la posicion 5,1 como bloqueados
        self.northBoard.board[6][1].rightBorder = False
        self.northBoard.board[5][1].rightBorder = False
        self.northBoard.board[6][1].leftBorder = False
        self.northBoard.board[5][1].leftBorder = False
        self.northBoard.board[5][1].topBorder = False
        self.northBoard.board[5][0].topBorder = False
        #Verifica que si el peon está en la posicion 5,1 o la posicion 6,1 está atrapado
        self.assertTrue(Wall.isTrapped(6,1,self.northBoard.board,'N'))
        self.assertTrue(Wall.isTrapped(5,1,self.northBoard.board,'N'))
        #Verifica que un peon sin paredes alrededor no está atrapado
        self.assertFalse(Wall.isTrapped(7,1,self.northBoard.board,'N'))

        #Inicia el tablero del lado sur
        self.southBoard.initBoard()
        #Mueve el peon de la posición 0,7 a la posicion 1,7
        self.southBoard.board[0][7].value = ' '
        self.southBoard.board[1][7].value = 'N'
        #Actualiza la posición de los peones
        self.southBoard.positionPawns()
        #Marca los bordes alrededor del peon en la posición 1,7 como bloqueados
        self.southBoard.board[2][7].rightBorder = False
        self.southBoard.board[3][7].rightBorder = False
        self.southBoard.board[2][7].leftBorder = False
        self.southBoard.board[3][7].leftBorder = False
        self.southBoard.board[3][7].botBorder = False
        self.southBoard.board[3][8].botBorder = False
        #Verifica que si el peón está en la posición 2,7 o 3,7 está atrapado
        self.assertTrue(Wall.isTrapped(2,7,self.southBoard.board,'S'))
        self.assertTrue(Wall.isTrapped(3,7,self.southBoard.board,'S'))
        #Verifica que peon sin paredes alrededor no está atrapado
        self.assertFalse(Wall.isTrapped(1,7,self.southBoard.board,'S'))
    
    def test_northSideWall(self):

        #Inicia el tablero del lado norte
        self.northBoard.initBoard()
        #Mueve el peon de la posicion 8,1 a la 7,1
        self.northBoard.board[8][1].value = ' '
        self.northBoard.board[7][1].value = 'S'
        #Actualiza el tablero
        self.northBoard.positionPawns()
        #Verifica que coloca la pared vertical derecha en el lugar correcto
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':4,'col':1,'orientation':'v'})
        #Marca los bordes afectados como bloqueados
        self.northBoard.board[4][1].rightBorder = False
        self.northBoard.board[5][1].rightBorder = False
        #Mueve el peon de la posicion 7,1 a la 6,1
        self.northBoard.board[7][1].value = ' '
        self.northBoard.board[6][1].value = 'S'
        #Actualiza la posición de los peones
        self.northBoard.positionPawns()
        #Verifica que coloca la pared vertical izquierda en el lugar correcto
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':4,'col':0,'orientation':'v'})
        #Marca los bordes afectados como bloqueados
        self.northBoard.board[4][1].leftBorder = False
        self.northBoard.board[5][1].leftBorder = False
        #Mueve el peon de la posicion 6,1 a la 5,1
        self.northBoard.board[6][1].value = ' '
        self.northBoard.board[5][1].value = 'S'
        #Actualiza la posición de los peones
        self.northBoard.positionPawns()
        #Verifica que coloca la pared horizontal en el lugar correcto
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':3,'col':1,'orientation':'h'})
        #Marca los bordes afectados como bloqueados
        self.northBoard.board[4][1].topBorder = False
        self.northBoard.board[4][2].topBorder = False
        #Mueve el peon de la posicion 8,4 a la 7,4
        self.northBoard.board[8][4].value = ' '
        self.northBoard.board[7][4].value = 'S'
        #Actualiza la posicion de los peones
        self.northBoard.positionPawns()
        #Verifica que coloca la pared vertical derecha correctamente
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':4,'col':4,'orientation':'v'})
        #Mueve el peon de la posicion 7,4 a la 6,4
        self.northBoard.board[7][4].value = ' '
        self.northBoard.board[6][4].value = 'S'
        #Mueve el peon de la posicion 8,7 a la 3,8 - No es posible pero es para verificar que prioriza al
        #peon más cerca de la meta
        self.northBoard.board[8][7].value = ' '
        self.northBoard.board[3][8].value = 'S'
        #Actualiza la posicion de los peones
        self.northBoard.positionPawns()
        #Verifica que coloca la pared vertical izquierda correctamente al peon más cerca de la meta(aprovecha los bordes del tablero)
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':1,'col':7,'orientation':'v'})
        #Marca los bordes afectados como bloqueados
        self.northBoard.board[1][8].leftBorder = False
        self.northBoard.board[2][8].leftBorder = False
        #Mueve el peon de la posicion 3,8 a la 2,8
        self.northBoard.board[3][8].value = ' '
        self.northBoard.board[2][8].value = 'S'
        #Actualiza la posicion de los peones
        self.northBoard.positionPawns()
        #Verifica que coloca la pared horizontal en el lugar correcto
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':0,'col':7,'orientation':'h'})



    def test_southSideWall(self):
        
        #Inicia el tablero del lado sur
        self.southBoard.initBoard()
        #Mueve el peon de la posicion 0,4 a la 1,4
        self.southBoard.board[0][4].value = ' '
        self.southBoard.board[1][4].value = 'N'
        #Actualiza la posicion de los peones
        self.southBoard.positionPawns()
        #Verfica que se coloque la pared vertical derecha correctamente
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':3,'col':4,'orientation':'v'})
        #Muve el peon de la posicion 1,4 a la 2,4
        self.southBoard.board[1][4].value = ' '
        self.southBoard.board[2][4].value = 'N'
        #Marca los bordes afectados por la pared como bloqueados
        self.southBoard.board[3][4].rightBorder = False
        self.southBoard.board[4][4].rightBorder = False
        #Actualiza la posicion de los peones
        self.southBoard.positionPawns()
        #Verifica que se coloque la pared vertical izquierda correctamente
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':3,'col':3,'orientation':'v'})
        #Mueve el peon de la posicion 2,4 a la 3,4
        self.southBoard.board[2][4].value = ' '
        self.southBoard.board[3][4].value = 'N'
        #Marca los bordes afectados por la pared como bloqueados
        self.southBoard.board[3][4].leftBorder = False
        self.southBoard.board[4][4].leftBorder = False
        #Actualiza la posicion de los peones
        self.southBoard.positionPawns()
        #Verifica que se coloque la pared horizontal correctamente
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':4,'col':3,'orientation':'h'})
        #Muve el peon de la posicion 0,1 a la 5,8
        self.southBoard.board[0][1].value = ' '
        self.southBoard.board[5][8].value = 'N'
        #Marca los bordes afectados por la pared horizontal como bloqueados
        self.southBoard.board[4][3].botBorder = False
        self.southBoard.board[4][4].botBorder = False
        #Actualiza la posicion de los peones
        self.southBoard.positionPawns()
        #Verifica que se coloque la pared vertical izquierda correctamente - Aprovechando los bordes del tablero
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':6,'col':7,'orientation':'v'})
        #Mueve el peon de la posicion 5,8 a la 6,8
        self.southBoard.board[5][8].value = ' '
        self.southBoard.board[6][8].value = 'N'
        #Marca los bordes afectados por la pared como bloqueados
        self.southBoard.board[6][8].leftBorder = False
        self.southBoard.board[7][8].leftBorder = False
        #Actualiza la posicion de los peones
        self.southBoard.positionPawns()
        #Verifica que se coloca la pared horizontal correctamente
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':7,'col':7,'orientation':'h'})
        
        




if __name__ == '__main__':
    unittest.main()