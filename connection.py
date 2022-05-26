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
                #print(f"Connection to {self.uri}")
                async with websockets.connect(self.uri) as websocket:
                    await self.play(websocket)
            except Exception:
                print("Conection error!")
                time.sleep(3)
    
    async def play(self, websocket):
        
        while True:
            try:
                request = await websocket.recv()
                #print(f"< {request}")
                request_data = json.loads(request)
                if request_data['event'] == 'list_users':
                    self.user_list = request_data['data']['users']
                    print("Updated user_list:")
                    for user in self.user_list:
                        print("                 "+ user)
                if request_data['event'] == 'game_over':
                    print("GAME OVER")
                    print(f"Player 1: {request_data['data']['player_1']} | Score: {request_data['data']['score_1']}")
                    print(f"Player 2: {request_data['data']['player_2']} | Score: {request_data['data']['score_2']}")
                    print("Winner: ", end="")
                    if float(request_data['data']['score_1']) > float(request_data['data']['score_2']):
                        print(request_data['data']['player_1'])
                    else:
                        print(request_data['data']['player_2'])

                if request_data['event'] == 'challenge':
                    await self.send(
                        websocket,
                        'accept_challenge',
                        {'challenge_id' : request_data['data']['challenge_id']}
                    )
                if request_data['event'] == 'your_turn':
                    print(f"Remaining turns: {request_data['data']['remaining_moves']}")
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
        print(f"Action: {action}")
        if action == 'wall':
            print(f"        row: {data['row']} col: {data['col']} orientation: {data['orientation']}")
        elif action == 'move':
            print(f"        from_row: {data['from_row']} to_row: {data['to_row']}")
            print(f"        from_col: {data['from_col']} to_col: {data['to_col']}")
        await websocket.send(message)