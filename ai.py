from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        gesture_selection = random.choice(self.gestures)
        return gesture_selection

    def get_name(self, name):
        names = ['Sunny', 'Orange', 'Mike', 'Lester']
        self.name = random.choice(names)


    
    
