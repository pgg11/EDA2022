import unittest
from pawn import Pawn
from board import PawnBoard

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.testBoard = PawnBoard('N')

    def test_initBoard(self):

        self.testBoard.initBoard()

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

        self.assertTrue(self.testBoard.board[0][1].rightBorder)
        self.assertTrue(self.testBoard.board[0][7].rightBorder)
        self.assertTrue(self.testBoard.board[3][5].rightBorder)
        self.assertTrue(self.testBoard.board[6][4].rightBorder)
        self.assertTrue(self.testBoard.board[8][0].rightBorder)
        self.assertTrue(self.testBoard.board[8][7].rightBorder)

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
        
        self.testBoard.initBoard()
        self.testBoard.positionPawns()

        self.assertEqual(self.testBoard.pawns[0].posY,0)
        self.assertEqual(self.testBoard.pawns[0].posX,1)
        self.assertEqual(self.testBoard.pawns[1].posY,0)
        self.assertEqual(self.testBoard.pawns[1].posX,4)
        self.assertEqual(self.testBoard.pawns[2].posY,0)
        self.assertEqual(self.testBoard.pawns[2].posX,7)
        
        self.assertEqual(self.testBoard.oppositePawns[0].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[0].posX,1)
        self.assertEqual(self.testBoard.oppositePawns[1].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[1].posX,4)
        self.assertEqual(self.testBoard.oppositePawns[2].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[2].posX,7)


        self.testBoard.board[0][1].value = ' '
        self.testBoard.board[0][4].value = ' '
        self.testBoard.board[0][7].value = ' '
        self.testBoard.board[8][1].value = ' '
        self.testBoard.board[8][4].value = ' '
        self.testBoard.board[8][7].value = ' '

        self.testBoard.board[2][5].value = 'N'
        self.testBoard.board[0][8].value = 'N'
        self.testBoard.board[5][7].value = 'N'
        self.testBoard.board[1][4].value = 'S'
        self.testBoard.board[6][6].value = 'S'
        self.testBoard.board[8][3].value = 'S'

        self.testBoard.positionPawns()

        self.assertEqual(self.testBoard.pawns[0].posY,0)
        self.assertEqual(self.testBoard.pawns[0].posX,8)
        self.assertEqual(self.testBoard.pawns[1].posY,2)
        self.assertEqual(self.testBoard.pawns[1].posX,5)
        self.assertEqual(self.testBoard.pawns[2].posY,5)
        self.assertEqual(self.testBoard.pawns[2].posX,7)

        self.assertEqual(self.testBoard.oppositePawns[0].posY,1)
        self.assertEqual(self.testBoard.oppositePawns[0].posX,4)
        self.assertEqual(self.testBoard.oppositePawns[1].posY,6)
        self.assertEqual(self.testBoard.oppositePawns[1].posX,6)
        self.assertEqual(self.testBoard.oppositePawns[2].posY,8)
        self.assertEqual(self.testBoard.oppositePawns[2].posX,3)

    def test_updatePawnBoard(self):

        self.testBoard.initBoard()

        self.testBoard.updatePawnBoard("              N N                                                -*-                             -*-            N                                                                     S                                              -*-                                                      S S")

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

        self.assertFalse(self.testBoard.board[1][7].botBorder)
        self.assertFalse(self.testBoard.board[1][8].botBorder)
        self.assertFalse(self.testBoard.board[2][6].botBorder)
        self.assertFalse(self.testBoard.board[2][7].botBorder)
        self.assertFalse(self.testBoard.board[2][7].topBorder)
        self.assertFalse(self.testBoard.board[6][4].botBorder)
        self.assertFalse(self.testBoard.board[6][5].botBorder)

        self.assertTrue(self.testBoard.board[1][2].botBorder)
        self.assertTrue(self.testBoard.board[7][7].topBorder)
        self.assertTrue(self.testBoard.board[4][7].rightBorder)
        self.assertTrue(self.testBoard.board[2][5].leftBorder)
        self.assertTrue(self.testBoard.board[7][4].botBorder)
        self.assertTrue(self.testBoard.board[3][1].topBorder)
        self.assertTrue(self.testBoard.board[5][6].rightBorder)
        self.assertTrue(self.testBoard.board[1][5].leftBorder)
    
    def test_processMove(self):

        self.testBoard.initBoard()
        self.assertIsInstance(self.testBoard.processMove(),dict)



        



if __name__ == '__main__':
    unittest.main()