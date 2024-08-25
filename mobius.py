import requests
import time
import random

URL        = "https://mobymon-api.mobysuite.com"
NAMESPACE  = "v1"
class Fight:

    def __init__(self):
        self.mobymon_id         = "MOBYMON_ID" # Make sure to fill out this field
        self.mode               = "training" # You can select 'training' to train or 'match' to play
        self.match_id           = "MATCH_ID" # Make sure to fill out this field
        self.last_opponent_move = None
        self.payload            = {"id": self.mobymon_id}
    
    def play(self):
        while True:
            status = self.status()
            if status['data']['status'] in ["round_pending", "round_playing"]:
                self.last_opponent_move = status['data'].get('previous_moves', {}).get('opponent')
                self.move(self.strategy())
                print("Wating for next round")
                time.sleep(1)

            elif status['data']['status'] == "match_end":
                print("Match ended")
                result = status['data']['final_score']
                break
        return result
        
    def move(self, attack: bool):
        move = "attack" if attack else "defend"
        response = requests.post(f"{URL}/{NAMESPACE}/{self.mode}/{self.match_id}/{move}", json=self.payload).json()
        if response['data']['status'] == "round_current_played":
            print(f"[MOVE] We are {'attacking' if attack else 'defending'}")
                
    def status(self):
        return requests.post(f"{URL}/{NAMESPACE}/{self.mode}/{self.match_id}/status", json=self.payload).json()
    
    def strategy(self):
        if self.last_opponent_move is True:
            return random.choice([True, False])
        else:
            return not self.last_opponent_move

if __name__ == "__main__":

    battle = Fight().play()
    
    if battle['you'] > battle['opponent']:
        print('Result: YOU WIN')
    elif battle['opponent'] > battle['you']:
        print('Result: YOU LOSE')
    else:
        print('Result: TIE')
    print('Battle result:', battle)
