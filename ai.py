from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = ['Sunny', 'Orange', 'Mike', 'Lester']
        super().__init__()

    def select_gesture(self):
        gesture_selection = random.choice(self.gestures)
        return gesture_selection

    def get_name(self):
        self.name = random.choice(self.name)


    
    
