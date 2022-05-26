import unittest
from board import PawnBoard

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.testBoard = PawnBoard('N')

    def test_initBoard(self):

        self.testBoard.initBoard()

        #Verifica que los peones estén en las posiciones iniciales
        #y que no haya peones en otros casilleros
        self.assertEqual(self.testBoard.board[0][0].value,' ')
        self.assertEqual(self.testBoard.board[0][1].value,'N')
        self.assertEqual(self.testBoard.board[0][4].value,'N')
        self.assertEqual(self.testBoard.board[0][7].value,'N')
        self.assertEqual(self.testBoard.board[0][5].value,' ')
        self.assertEqual(self.testBoard.board[0][8].value,' ')
        self.assertEqual(self.testBoard.board[3][3].value,' ')
        self.assertEqual(self.testBoard.board[2][6].value,' ')
        self.assertEqual(self.testBoard.board[6][3].value,' ')
        self.assertEqual(self.testBoard.board[0][8].value,' ')
        self.assertEqual(self.testBoard.board[8][1].value,'S')
        self.assertEqual(self.testBoard.board[8][4].value,'S')
        self.assertEqual(self.testBoard.board[8][7].value,'S')
        self.assertEqual(self.testBoard.board[8][6].value,' ')
        self.assertEqual(self.testBoard.board[8][8].value,' ')

        #Verifica que lo bordes derechos de los casilleros antes
        #de la columna 8 estén marcados como True
        self.assertTrue(self.testBoard.board[0][1].rightBorder)
        self.assertTrue(self.testBoard.board[0][7].rightBorder)
        self.assertTrue(self.testBoard.board[3][5].rightBorder)
        self.assertTrue(self.testBoard.board[6][4].rightBorder)
        self.assertTrue(self.testBoard.board[8][0].rightBorder)
        self.assertTrue(self.testBoard.board[8][7].rightBorder)

        #Verifica que los borodes del tablero estén correctamente marcados
        #con False
        self.assertFalse(self.testBoard.board[0][0].leftBorder)
        self.assertFalse(self.testBoard.board[3][0].leftBorder)
        self.assertFalse(self.testBoard.board[5][0].leftBorder)
        self.assertFalse(self.testBoard.board[8][0].leftBorder)
        self.assertFalse(self.testBoard.board[0][0].topBorder)
        self.assertFalse(self.testBoard.board[0][3].topBorder)
        self.assertFalse(self.testBoard.board[0][5].topBorder)
        self.assertFalse(self.testBoard.board[0][8].topBorder)
        self.assertFalse(self.testBoard.board[0][8].rightBorder)
        self.assertFalse(self.testBoard.board[4][8].rightBorder)
        self.assertFalse(self.testBoard.board[6][8].rightBorder)
        self.assertFalse(self.testBoard.board[8][8].rightBorder)
        self.assertFalse(self.testBoard.board[8][0].botBorder)
        self.assertFalse(self.testBoard.board[8][3].botBorder)
        self.assertFalse(self.testBoard.board[8][5].botBorder)
        self.assertFalse(self.testBoard.board[8][8].botBorder)
    
    def test_positionPawns(self):
        #Marca los bordes del tablero y ubica los peones en las posiciones iniciales
        self.testBoard.initBoard()
        self.testBoard.positionPawns()

        #Verifica que los peones estén en las posiciones correspondientes
        self.assertEqual(self.testBoard.pawns[0].posY,0)
        self.assertEqual(self.testBoard.pawns[0].posX,1)
        self.assertEqual(self.testBoard.pawns[1].posY,0)
        self.assertEqual(self.testBoard.pawns[1].posX,4)
        self.assertEqual(self.testBoard.pawns[2].posY,0)
        self.assertEqual(self.testBoard.pawns[2].posX,7)
        #verifica que los peones contrarios estén en las posiciones correspondientes
        self.assertEqual(self.testBoard.oppositePawns[0].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[0].posX,1)
        self.assertEqual(self.testBoard.oppositePawns[1].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[1].posX,4)
        self.assertEqual(self.testBoard.oppositePawns[2].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[2].posX,7)

        #Quita los peones de los lugares iniciales
        self.testBoard.board[0][1].value = ' '
        self.testBoard.board[0][4].value = ' '
        self.testBoard.board[0][7].value = ' '
        self.testBoard.board[8][1].value = ' '
        self.testBoard.board[8][4].value = ' '
        self.testBoard.board[8][7].value = ' '
        #Ubica los peones en otros lugares aleatorios
        self.testBoard.board[2][5].value = 'N'
        self.testBoard.board[0][8].value = 'N'
        self.testBoard.board[5][7].value = 'N'
        self.testBoard.board[1][4].value = 'S'
        self.testBoard.board[6][6].value = 'S'
        self.testBoard.board[8][3].value = 'S'
        #Se llama a la funciona para actualizar la posición de los peones
        self.testBoard.positionPawns()
        #Verifica que los peones hayan sido ubicados correctamente
        self.assertEqual(self.testBoard.pawns[0].posY,0)
        self.assertEqual(self.testBoard.pawns[0].posX,8)
        self.assertEqual(self.testBoard.pawns[1].posY,2)
        self.assertEqual(self.testBoard.pawns[1].posX,5)
        self.assertEqual(self.testBoard.pawns[2].posY,5)
        self.assertEqual(self.testBoard.pawns[2].posX,7)
        #Verifica que los peones contratios hayan sido ubicados correctamente
        self.assertEqual(self.testBoard.oppositePawns[0].posY,1)
        self.assertEqual(self.testBoard.oppositePawns[0].posX,4)
        self.assertEqual(self.testBoard.oppositePawns[1].posY,6)
        self.assertEqual(self.testBoard.oppositePawns[1].posX,6)
        self.assertEqual(self.testBoard.oppositePawns[2].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[2].posX,3)

    def test_updatePawnBoard(self):

        self.testBoard.initBoard()

        #Actualiza el tablero al tablero que está debajo
        self.testBoard.updatePawnBoard("              N N                                                -*-                             -*-            N                                                                     S                                              -*-                                                      S S")

        #     0a1b2c3d4e5f6g7h8
        #     -----------------
        #   0|              N N
        #   a|                 
        #   1|                 
        #   b|              -*-
        #   2|                 
        #   c|            -*-  
        #   3|          N      
        #   d|                 
        #   4|                 
        #   e|                 
        #   5|            S    
        #   f|                 
        #   6|                 
        #   g|        -*-      
        #   7|                 
        #   h|                 
        #   8|              S S

        #Verifica que los pones estén en las posiciones conrrectas despues de actualizar el tablero
        self.assertEqual(self.testBoard.board[0][1].value,' ')
        self.assertEqual(self.testBoard.board[0][7].value,'N')
        self.assertEqual(self.testBoard.board[0][8].value,'N')
        self.assertEqual(self.testBoard.board[3][5].value,'N')
        self.assertEqual(self.testBoard.board[3][6].value,' ')
        self.assertEqual(self.testBoard.board[8][0].value,' ')
        self.assertEqual(self.testBoard.board[7][7].value,' ')
        self.assertEqual(self.testBoard.board[5][6].value,'S')
        self.assertEqual(self.testBoard.board[8][7].value,'S')
        self.assertEqual(self.testBoard.board[8][8].value,'S')
        #Verifica que se detecten correctamente las paredes horizontales
        #marcando como falso los bordes afectados
        self.assertFalse(self.testBoard.board[1][7].botBorder)
        self.assertFalse(self.testBoard.board[1][8].botBorder)
        self.assertFalse(self.testBoard.board[2][6].botBorder)
        self.assertFalse(self.testBoard.board[2][7].botBorder)
        self.assertFalse(self.testBoard.board[2][7].topBorder)
        self.assertFalse(self.testBoard.board[6][4].botBorder)
        self.assertFalse(self.testBoard.board[6][5].botBorder)
        #Verifica que no se hayan marcado bordes no afectados
        self.assertTrue(self.testBoard.board[0][7].botBorder)
        self.assertTrue(self.testBoard.board[7][7].topBorder)
        self.assertTrue(self.testBoard.board[4][7].rightBorder)
        self.assertTrue(self.testBoard.board[2][5].leftBorder)
        self.assertTrue(self.testBoard.board[7][4].botBorder)
        self.assertTrue(self.testBoard.board[3][1].topBorder)
        self.assertTrue(self.testBoard.board[5][6].rightBorder)
        self.assertTrue(self.testBoard.board[1][5].leftBorder)
        
        #Se actualiza con otro tablero diferente
        self.testBoard.updatePawnBoard("  N     N                                                                  | |              * *              | |   | |         -*-  * *             N| |       -*-     -*-        S                                                                              -*-                    S     S  ")

        #     0a1b2c3d4e5f6g7h8
        #     -----------------
        #   0|  N     N        
        #   a|                 
        #   1|                 
        #   b|                 
        #   2|       | |       
        #   c|       * *       
        #   3|       | |   | | 
        #   d|        -*-  * * 
        #   4|            N| | 
        #   e|      -*-     -*-
        #   5|        S        
        #   f|                 
        #   6|                 
        #   g|                 
        #   7|                 
        #   h|  -*-            
        #   8|        S     S  

        #Verifica nuevamente que los peones sean localizados correctamente
        self.assertEqual(self.testBoard.board[0][1].value,'N')
        self.assertEqual(self.testBoard.board[0][4].value,'N')
        self.assertEqual(self.testBoard.board[0][7].value,' ')
        self.assertEqual(self.testBoard.board[4][6].value,'N')
        self.assertEqual(self.testBoard.board[1][8].value,' ')
        self.assertEqual(self.testBoard.board[8][4].value,'S')
        self.assertEqual(self.testBoard.board[8][7].value,'S')
        self.assertEqual(self.testBoard.board[5][4].value,'S')
        #Verifica que se marquen los bordes afectados por las paredes
        self.assertFalse(self.testBoard.board[2][3].rightBorder)
        self.assertFalse(self.testBoard.board[3][3].rightBorder)
        self.assertFalse(self.testBoard.board[2][4].leftBorder)
        self.assertFalse(self.testBoard.board[2][4].rightBorder)
        self.assertFalse(self.testBoard.board[2][5].leftBorder)
        self.assertFalse(self.testBoard.board[3][4].botBorder)
        self.assertFalse(self.testBoard.board[3][4].leftBorder)
        self.assertFalse(self.testBoard.board[3][4].rightBorder)
        self.assertFalse(self.testBoard.board[3][5].leftBorder)
        self.assertFalse(self.testBoard.board[4][4].topBorder)
        self.assertFalse(self.testBoard.board[4][6].rightBorder)
        self.assertFalse(self.testBoard.board[5][7].topBorder)
        self.assertFalse(self.testBoard.board[5][8].topBorder)
            


    def test_processMove(self):

        #Inicio el tablero con los peones en las posiciones iniciales
        self.testBoard.initBoard()
        #Verifica que el procesamiento de movimiento me retorne un diccionario
        #que es la forma en que envia el movimiento
        self.assertIsInstance(self.testBoard.processMove(),dict)
    
    def test_processWall(self):
        
        self.testBoard.initBoard()
        #Se cambia de lugar un peon contrario para que el procesamiento de pared
        #retorne una posicion de pared, ya que coloca paredes a peones que hayan avanzado
        #por lo menos un casillero
        self.testBoard.board[8][1].value = ' '
        self.testBoard.board[7][1].value = 'S'
        #Verifica que el procesamiento de pared me retorne un diccionario
        #que es la forma en la que se envia la pared
        self.assertIsInstance(self.testBoard.processWall(),dict)





if __name__ == '__main__':
    unittest.main()