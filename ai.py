from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = 'Sunny'
        super().__init__()

    def select_gesture(self):
        super().select_gesture(self.name)
        gesture_selection = random.choice(self.gestures)
        print(f'{self.name} plays: {gesture_selection}!')

    
    
