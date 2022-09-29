

class Player:
    def __init__(self):

        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    
    def select_gesture(self, player_name):
        i = 0
        for gesture in self.gestures:
            i += 1
            print(f'[{i}] {gesture}')     
        gesture_selection = int(input(f'Select your move: '))

        gesture_index = gesture_selection - 1
        gesture = self.gestures[gesture_index]
        print(f'{player_name} plays: {gesture}!')