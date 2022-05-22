import unittest
from wall import Wall
from board import PawnBoard


class TestWall(unittest.TestCase):

    def setUp(self):
        self.board = PawnBoard('N').board
        self.northBoard = PawnBoard('N')
        self.southBoard = PawnBoard('S')

    def test_checkWallPosition(self):

        self.assertFalse(Wall.checkWallPosition(8,5,'v',self.board))
        self.assertFalse(Wall.checkWallPosition(4,8,'h',self.board))
        self.assertFalse(Wall.checkWallPosition(0,8,'v',self.board))
        self.assertFalse(Wall.checkWallPosition(8,8,'h',self.board))

        self.board[4][4].botBorder = False
        self.board[4][5].botBorder = False

        self.assertFalse(Wall.checkWallPosition(4,4,'v',self.board))

        self.board[2][6].rightBorder = False
        self.board[3][6].rightBorder = False

        self.assertFalse(Wall.checkWallPosition(2,6,'h',self.board))

        self.assertTrue(Wall.checkWallPosition(0,2,'h',self.board))
        self.assertTrue(Wall.checkWallPosition(0,0,'v',self.board))
        self.assertTrue(Wall.checkWallPosition(4,3,'v',self.board))
        self.assertTrue(Wall.checkWallPosition(4,6,'v',self.board))
        self.assertTrue(Wall.checkWallPosition(1,6,'h',self.board))
        self.assertTrue(Wall.checkWallPosition(7,7,'h',self.board))
        self.assertTrue(Wall.checkWallPosition(7,3,'v',self.board))
    
    def test_wallPosition(self):

        self.assertEqual(Wall.wallPosition(2,5,'v'),{'row':2,'col':5,'orientation':'v'})
        self.assertEqual(Wall.wallPosition(7,7,'v'),{'row':7,'col':7,'orientation':'v'})
        self.assertEqual(Wall.wallPosition(0,0,'v'),{'row':0,'col':0,'orientation':'v'})
        self.assertEqual(Wall.wallPosition(4,7,'h'),{'row':4,'col':7,'orientation':'h'})
        self.assertEqual(Wall.wallPosition(0,7,'h'),{'row':0,'col':7,'orientation':'h'})
        self.assertEqual(Wall.wallPosition(7,0,'h'),{'row':7,'col':0,'orientation':'h'})

        self.assertEqual(Wall.wallPosition(8,3,'v'),'Invalid position')
        self.assertEqual(Wall.wallPosition(0,8,'v'),'Invalid position')
        self.assertEqual(Wall.wallPosition(8,8,'h'),'Invalid position')
        self.assertEqual(Wall.wallPosition(8,6,'h'),'Invalid position')
    
    def test_isTrapped(self):

        self.northBoard.initBoard()
        self.northBoard.board[8][1].value = ' '
        self.northBoard.board[5][1].value = 'S'
        self.northBoard.positionPawns()
        self.northBoard.board[6][1].rightBorder = False
        self.northBoard.board[5][1].rightBorder = False
        self.northBoard.board[6][1].leftBorder = False
        self.northBoard.board[5][1].leftBorder = False
        self.northBoard.board[5][1].topBorder = False
        self.northBoard.board[5][0].topBorder = False

        self.assertTrue(Wall.isTrapped(6,1,self.northBoard.board,'N'))
        self.assertTrue(Wall.isTrapped(5,1,self.northBoard.board,'N'))
        self.assertFalse(Wall.isTrapped(7,1,self.northBoard.board,'N'))

        self.southBoard.initBoard()
        self.southBoard.board[0][7].value = ' '
        self.southBoard.board[1][7].value = 'N'
        self.southBoard.positionPawns()
        self.southBoard.board[2][7].rightBorder = False
        self.southBoard.board[3][7].rightBorder = False
        self.southBoard.board[2][7].leftBorder = False
        self.southBoard.board[3][7].leftBorder = False
        self.southBoard.board[3][7].botBorder = False
        self.southBoard.board[3][8].botBorder = False

        self.assertTrue(Wall.isTrapped(2,7,self.southBoard.board,'S'))
        self.assertTrue(Wall.isTrapped(3,7,self.southBoard.board,'S'))
        self.assertFalse(Wall.isTrapped(1,7,self.southBoard.board,'S'))
    
    def test_northSideWall(self):

        self.northBoard.initBoard()
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':5,'col':1,'orientation':'v'})
        self.northBoard.board[5][1].rightBorder = False
        self.northBoard.board[6][1].rightBorder = False
        self.northBoard.board[8][1].value = ' '
        self.northBoard.board[7][1].value = 'S'
        self.northBoard.positionPawns()
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':5,'col':0,'orientation':'v'})
        self.northBoard.board[5][1].leftBorder = False
        self.northBoard.board[6][1].leftBorder = False
        self.southBoard.board[5][0].rightBorder = False
        self.southBoard.board[6][0].rightBorder = False
        self.northBoard.board[7][1].value = ' '
        self.northBoard.board[6][1].value = 'S'
        self.northBoard.positionPawns()
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':4,'col':1,'orientation':'h'})
        self.northBoard.board[5][1].topBorder = False
        self.northBoard.board[5][2].topBorder = False
        self.northBoard.board[6][1].value = ' '
        self.northBoard.board[5][1].value = 'S'
        self.assertEqual(Wall.northSideWall(self.northBoard.board,self.northBoard.oppositePawns),{'row':5,'col':4,'orientation':'v'})

    def test_southSideWall(self):


        self.southBoard.initBoard()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':2,'col':7,'orientation':'v'})
        self.southBoard.board[0][4].value = ' '
        self.southBoard.board[1][4].value = 'N'
        self.southBoard.board[2][7].rightBorder = False
        self.southBoard.board[3][7].rightBorder = False
        self.southBoard.positionPawns()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':3,'col':4,'orientation':'v'})
        self.southBoard.board[1][4].value = ' '
        self.southBoard.board[2][4].value = 'N'
        self.southBoard.board[3][4].rightBorder = False
        self.southBoard.board[4][4].rightBorder = False
        self.southBoard.positionPawns()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':3,'col':3,'orientation':'v'})
        self.southBoard.board[2][4].value = ' '
        self.southBoard.board[3][4].value = 'N'
        self.southBoard.board[3][4].leftBorder = False
        self.southBoard.board[4][4].leftBorder = False
        self.southBoard.positionPawns()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':4,'col':4,'orientation':'h'})
        self.southBoard.board[3][4].value = ' '
        self.southBoard.board[4][4].value = 'N'
        self.southBoard.board[4][4].botBorder = False
        self.southBoard.board[4][5].botBorder = False
        self.southBoard.positionPawns()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':2,'col':6,'orientation':'v'})
        self.southBoard.board[0][7].value = ' '
        self.southBoard.board[1][7].value = 'N'
        self.southBoard.board[2][7].leftBorder = False
        self.southBoard.board[3][7].leftBorder = False
        self.southBoard.positionPawns()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':3,'col':7,'orientation':'h'})
        self.southBoard.board[1][7].value = ' '
        self.southBoard.board[2][7].value = 'N'
        self.southBoard.board[3][7].botBorder = False
        self.southBoard.board[3][8].botBorder = False
        self.southBoard.positionPawns()
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':2,'col':1,'orientation':'v'})
        self.southBoard.board[2][1].rightBorder = False
        self.southBoard.board[3][1].rightBorder = False
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':2,'col':0,'orientation':'v'})
        self.southBoard.board[2][1].leftBorder = False
        self.southBoard.board[3][1].leftBorder = False
        self.assertEqual(Wall.southSideWall(self.southBoard.board,self.southBoard.oppositePawns),{'row':3,'col':1,'orientation':'h'})



        




if __name__ == '__main__':
    unittest.main()