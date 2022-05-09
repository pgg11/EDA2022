import websockets
import time
import json
import game

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
                if request_data['event'] == 'update_user_list':
                    self.user_list = request_data['data']['users']
                    print(f"Updated user_list: {self.user_list}")
                if request_data['event'] == 'gameover':
                    pass
                if request_data['event'] == 'challenge':
                    await self.send(
                        websocket,
                        'accept_challenge',
                        {
                            'challenge_id' : request_data['data']['challenge_id']
                        }
                    )
                if request_data['event'] == 'your_turn':
                    #Si el id no está en games, se crea un juego y se agrega
                    if not self.games[request_data['data']['game_id']]:
                        self.games['game_id'] =  game.Game(request_data['data'])
                    #Si se encuentra, actualiza la info
                    else:
                        self.games['game_id'].update_status(request_data['data'])
                    self.games['game_id'].show_board()

                    ##continuar##
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