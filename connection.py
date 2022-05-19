import websockets
import time
import json
from game import Game

class Connection():

    def __init__(self,token):

        self.uri = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={token}"
        self.user_list = list()
        self.games = dict()

    async def start(self):
        
        while True:
            try:
                print(f"Connection to {self.uri}")
                async with websockets.connect(self.uri) as websocket:
                    await self.play(websocket)
            except Exception:
                print("Conection error!")
                time.sleep(3)
    
    async def play(self, websocket):
        
        while True:
            try:
                request = await websocket.recv()
                print(f"< {request}")
                request_data = json.loads(request)
                if request_data['event'] == 'user_list':
                    pass
                    #self.user_list = request_data['data']['users']
                    #print(f"Updated user_list: {self.user_list}")
                if request_data['event'] == 'gameover':
                    pass
                if request_data['event'] == 'challenge':
                    await self.send(
                        websocket,
                        'accept_challenge',
                        {'challenge_id' : request_data['data']['challenge_id']}
                    )
                if request_data['event'] == 'your_turn':
                    #Si el id no está en games, se crea un juego y se agrega
                    game_id = request_data['data']['game_id']
                    if self.games.get(game_id) == None:
                        self.games[game_id] =  Game(request_data['data'])
                    #Si se encuentra, actualiza la info
                    else:
                        self.games[game_id].update_status(request_data['data'])
                    #Imprime el tablero
                    self.games[game_id].show_board()
                    #Realiza acción
                    move = self.games[game_id].process_your_turn()
                    #Verifica acción y la envía
                    if len(move) == 4:
                        await self.send(
                            websocket,
                            'move',
                            {
                                'game_id': request_data['data']['game_id'],
                                'turn_token': request_data['data']['turn_token'],
                                'from_row': move['from_row'],
                                'from_col': move['from_col'],
                                'to_row': move['to_row'],
                                'to_col': move['to_col'],
                            },
                        )
                    else:
                        await self.send(
                            websocket,
                            'wall',
                            {
                                'game_id': request_data['data']['game_id'],
                                'turn_token': request_data['data']['turn_token'],
                                'row': move['row'],
                                'col': move['col'],
                                'orientation': move['orientation'],
                            }
                        )
            except Exception:
                print(f"Error {Exception}")
                break  
    
    async def send(self,websocket,action,data):
        message = json.dumps(
            {
                'action' : action,
                'data' : data,
            }
        )
        print(message)
        await websocket.send(message)