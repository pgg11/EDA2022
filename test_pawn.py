import unittest
from pawn import Pawn
from board import PawnBoard

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.northBoard = PawnBoard('N')
        self.southBoard = PawnBoard('S')

    def test_moveForward(self):
        self.assertEqual(Pawn.moveForward(0,0,'N'),{'from_row':0,'from_col':0,'to_row':1,'to_col':0})
        self.assertEqual(Pawn.moveForward(7,8,'N'),{'from_row':7,'from_col':8,'to_row':8,'to_col':8})
        self.assertEqual(Pawn.moveForward(4,4,'N'),{'from_row':4,'from_col':4,'to_row':5,'to_col':4})
        self.assertEqual(Pawn.moveForward(8,1,'S'),{'from_row':8,'from_col':1,'to_row':7,'to_col':1})
        self.assertEqual(Pawn.moveForward(1,3,'S'),{'from_row':1,'from_col':3,'to_row':0,'to_col':3})
        self.assertEqual(Pawn.moveForward(4,8,'S'),{'from_row':4,'from_col':8,'to_row':3,'to_col':8})

    def test_checkLeftSide(self):

        self.northBoard.initBoard()
        self.northBoard.board[4][4].value = 'N'
        self.northBoard.board[4][4].leftBorder = False
        self.northBoard.board[6][3].value = 'N'
        self.northBoard.board[6][2].value = 'N'
        self.northBoard.board[2][0].value = 'N'

        self.assertTrue(Pawn.checkLeftSide(self.northBoard.board,0,1,{}))
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,0,7,{'from_row': 0, 'from_col': 6}))
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,4,4,{}))
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,6,3,{}))
        self.assertFalse(Pawn.checkLeftSide(self.northBoard.board,2,0,{}))
    
    def test_checkRightSide(self):

        self.southBoard.initBoard()
        self.southBoard.board[4][4].value = 'S'
        self.southBoard.board[4][4].rightBorder = False
        self.southBoard.board[6][3].value = 'S'
        self.southBoard.board[6][2].value = 'S'
        self.southBoard.board[2][8].value = 'S'

        self.assertTrue(Pawn.checkRightSide(self.southBoard.board,8,1,{}))
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,8,7,{'from_row': 8, 'from_col': 8}))
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,4,4,{}))
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,6,2,{}))
        self.assertFalse(Pawn.checkRightSide(self.southBoard.board,2,8,{}))
    
    def test_checkJump(self):
        
        self.northBoard.initBoard()
        self.northBoard.board[1][1].value = 'S'
        self.northBoard.board[1][7].value = 'S'
        self.northBoard.board[1][7].botBorder = False
        self.northBoard.board[6][5].value = 'N'
        self.northBoard.board[6][6].value = 'S'

        self.assertTrue(Pawn.checkJump(self.northBoard.board,0,1,self.northBoard.side))
        self.assertFalse(Pawn.checkJump(self.northBoard.board,0,7,self.northBoard.side))
        self.assertTrue(Pawn.checkJump(self.northBoard.board,6,5,self.northBoard.side))        
        
        self.southBoard.initBoard()
        self.southBoard.board[7][1].value = 'N'
        self.southBoard.board[7][7].value = 'N'
        self.southBoard.board[7][7].topBorder = False
        self.southBoard.board[2][6].value = 'N'
        self.southBoard.board[3][6].value = 'S'

        self.assertTrue(Pawn.checkJump(self.southBoard.board,8,1,self.southBoard.side))
        self.assertFalse(Pawn.checkJump(self.southBoard.board,8,7,self.southBoard.side))
        self.assertTrue(Pawn.checkJump(self.southBoard.board,3,6,self.southBoard.side))
    
    def test_checkRightDiagonalJump(self):
        self.northBoard.initBoard()
        self.northBoard.board[2][3].value = 'N'
        self.northBoard.board[3][3].value = 'S'
        self.northBoard.board[3][3].botBorder = False
        self.northBoard.board[4][4].value = 'N'
        self.northBoard.board[5][4].value = 'S'
        self.northBoard.board[5][4].botBorder = False
        self.northBoard.board[5][5].leftBorder = False

        self.assertTrue(Pawn.checkRightDiagonalJump(self.northBoard.board,2,3,self.northBoard.side))
        self.assertFalse(Pawn.checkRightDiagonalJump(self.northBoard.board,4,4,self.northBoard.side))       
        
        self.southBoard.initBoard()
        self.southBoard.board[7][1].value = 'N'
        self.southBoard.board[7][1].topBorder = False
        self.southBoard.board[4][4].value = 'N'
        self.southBoard.board[5][4].value = 'S'
        self.southBoard.board[4][4].topBorder = False
        self.southBoard.board[4][5].leftBorder = False

        self.assertTrue(Pawn.checkRightDiagonalJump(self.southBoard.board,8,1,self.southBoard.side))
        self.assertFalse(Pawn.checkRightDiagonalJump(self.southBoard.board,5,4,self.southBoard.side))

    def test_checkLeftDiagonalJump(self):
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
        self.assertEqual(Pawn.moveToLeft(0,1),{'from_row':0,'from_col':1,'to_row':0,'to_col':0})
        self.assertEqual(Pawn.moveToLeft(0,8),{'from_row':0,'from_col':8,'to_row':0,'to_col':7})
        self.assertEqual(Pawn.moveToLeft(4,4),{'from_row':4,'from_col':4,'to_row':4,'to_col':3})
        self.assertEqual(Pawn.moveToLeft(8,1),{'from_row':8,'from_col':1,'to_row':8,'to_col':0})
        self.assertEqual(Pawn.moveToLeft(8,8),{'from_row':8,'from_col':8,'to_row':8,'to_col':7})
        self.assertEqual(Pawn.moveToLeft(2,2),{'from_row':2,'from_col':2,'to_row':2,'to_col':1})
    
    def test_moveToRight(self):
        self.assertEqual(Pawn.moveToRight(0,1),{'from_row':0,'from_col':1,'to_row':0,'to_col':2})
        self.assertEqual(Pawn.moveToRight(0,7),{'from_row':0,'from_col':7,'to_row':0,'to_col':8})
        self.assertEqual(Pawn.moveToRight(4,4),{'from_row':4,'from_col':4,'to_row':4,'to_col':5})
        self.assertEqual(Pawn.moveToRight(8,1),{'from_row':8,'from_col':1,'to_row':8,'to_col':2})
        self.assertEqual(Pawn.moveToRight(8,0),{'from_row':8,'from_col':0,'to_row':8,'to_col':1})
        self.assertEqual(Pawn.moveToRight(2,2),{'from_row':2,'from_col':2,'to_row':2,'to_col':3})
    
    def test_jumpSouthPawn(self):
        self.assertEqual(Pawn.jumpSouthPawn(0,1),{'from_row':0,'from_col':1,'to_row':2,'to_col':1})
        self.assertEqual(Pawn.jumpSouthPawn(0,8),{'from_row':0,'from_col':8,'to_row':2,'to_col':8})
        self.assertEqual(Pawn.jumpSouthPawn(4,4),{'from_row':4,'from_col':4,'to_row':6,'to_col':4})
        self.assertEqual(Pawn.jumpSouthPawn(6,8),{'from_row':6,'from_col':8,'to_row':8,'to_col':8})
        self.assertEqual(Pawn.jumpSouthPawn(6,0),{'from_row':6,'from_col':0,'to_row':8,'to_col':0})
        self.assertEqual(Pawn.jumpSouthPawn(4,5),{'from_row':4,'from_col':5,'to_row':6,'to_col':5})
    
    def test_jumpNorthPawn(self):
        self.assertEqual(Pawn.jumpNorthPawn(2,1),{'from_row':2,'from_col':1,'to_row':0,'to_col':1})
        self.assertEqual(Pawn.jumpNorthPawn(2,8),{'from_row':2,'from_col':8,'to_row':0,'to_col':8})
        self.assertEqual(Pawn.jumpNorthPawn(4,4),{'from_row':4,'from_col':4,'to_row':2,'to_col':4})
        self.assertEqual(Pawn.jumpNorthPawn(5,8),{'from_row':5,'from_col':8,'to_row':3,'to_col':8})
        self.assertEqual(Pawn.jumpNorthPawn(6,0),{'from_row':6,'from_col':0,'to_row':4,'to_col':0})
        self.assertEqual(Pawn.jumpNorthPawn(4,5),{'from_row':4,'from_col':5,'to_row':2,'to_col':5})
    
    def test_leftDiagonalJump(self):
        self.assertEqual(Pawn.leftDiagonalJump(0,8,'N'),{'from_row':0,'from_col':8,'to_row':1,'to_col':7})
        self.assertEqual(Pawn.leftDiagonalJump(3,3,'N'),{'from_row':3,'from_col':3,'to_row':4,'to_col':2})
        self.assertEqual(Pawn.leftDiagonalJump(6,8,'N'),{'from_row':6,'from_col':8,'to_row':7,'to_col':7})
        self.assertEqual(Pawn.leftDiagonalJump(3,1,'S'),{'from_row':3,'from_col':1,'to_row':2,'to_col':0})
        self.assertEqual(Pawn.leftDiagonalJump(4,4,'S'),{'from_row':4,'from_col':4,'to_row':3,'to_col':3})
        self.assertEqual(Pawn.leftDiagonalJump(8,8,'S'),{'from_row':8,'from_col':8,'to_row':7,'to_col':7})
    
    def test_rightDiagonalJump(self):
        self.assertEqual(Pawn.rightDiagonalJump(0,0,'N'),{'from_row':0,'from_col':0,'to_row':1,'to_col':1})
        self.assertEqual(Pawn.rightDiagonalJump(3,3,'N'),{'from_row':3,'from_col':3,'to_row':4,'to_col':4})
        self.assertEqual(Pawn.rightDiagonalJump(6,7,'N'),{'from_row':6,'from_col':7,'to_row':7,'to_col':8})
        self.assertEqual(Pawn.rightDiagonalJump(3,7,'S'),{'from_row':3,'from_col':7,'to_row':2,'to_col':8})
        self.assertEqual(Pawn.rightDiagonalJump(4,4,'S'),{'from_row':4,'from_col':4,'to_row':3,'to_col':5})
        self.assertEqual(Pawn.rightDiagonalJump(8,0,'S'),{'from_row':8,'from_col':0,'to_row':7,'to_col':1})


if __name__ == '__main__':
    unittest.main()