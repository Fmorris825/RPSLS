

class Player:
    def __init__(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    
    def select_gesture(self, player_name):
        i = 0
        for gesture in self.gestures:
            i += 1
            print(f'[{i}] {gesture}')     
        gesture_selection = input(f'Select your move: ')

        while gesture_selection != '1' and gesture_selection != '2' and gesture_selection != '3' and gesture_selection != '4' and gesture_selection != '5':
            print('Invalid')
            gesture_selection = input(f'Select your move: ')

        gesture_selection = int(gesture_selection)
        gesture_index = gesture_selection - 1
        gesture = self.gestures[gesture_index]
        
        return gesture

    def get_name(self):
        self.name = input(f'\nWhat is your name? ')
        
        
