import unittest
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        #Inicializa un tablero para los casos de prueba
        self.game = Game({"score_2": 0.0, "walls": 10.0, "player_1": "player1@gmail.com", "board": "  N     N                                       N                                                                                                                                                                                                                                 S     S     S  ", "remaining_moves": 199.0, "score_1": 2.0, "side": "S", "player_2": "player2@gmail.com", "turn_token": "4733937e-df2e-45b7-a16e-cd6e33b73f2e", "game_id": "5277f81c-d701-11ec-aef0-7ecdf393f9cc"})

    def test_updateStatus(self):

        #Verifica que los valores de Game sean los correspondientes
        self.assertEqual(self.game.score1,2.0)
        self.assertEqual(self.game.score2,0.0)
        self.assertEqual(self.game.remaining_moves,199.0)
        self.assertEqual(self.game.walls,10)
        self.assertEqual(self.game.strBoard,"  N     N                                       N                                                                                                                                                                                                                                 S     S     S  ")

        #Actualiza el estado de Game
        self.game.update_status({"remaining_moves": 197.0, "player_2": "player2@gmail.com", "score_2": 2.0, "side": "S", "board": "  N     N                                                                         N                                                                                                                                                             S                                       S     S  ", "player_1": "player1@gmail.com", "score_1": 6.0, "walls": 10.0, "turn_token": "2cc6d918-9f4a-483b-93c2-183917da1698", "game_id": "5277f81c-d701-11ec-aef0-7ecdf393f9cc"})
        
        #Verifica que los valores se hayan actualizado correctamente
        self.assertEqual(self.game.score1,6.0)
        self.assertEqual(self.game.score2,2.0)
        self.assertEqual(self.game.remaining_moves,197.0)
        self.assertEqual(self.game.walls,10)
        self.assertEqual(self.game.strBoard,"  N     N                                                                         N                                                                                                                                                             S                                       S     S  ")





if __name__ == '__main__':
    unittest.main()