from ai import AI

class Player:
    def __init__(self):
        self.player1 = ''
        self.player2 = ''
        self.ai = AI()
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    
    def select_gesture(self):
        i = 0
        for gesture in self.gestures:
            i += 1
            print(f'{[i]} {gesture}')
            
        gesture_selection = int(input('Select your move: '))

        gesture_index = gesture_selection - 1
        gesture = self.gestures[gesture_index]
        return gesture