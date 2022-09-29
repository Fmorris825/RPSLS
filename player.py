

class Player:
    def __init__(self):
        self.name = ''
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.points = 0
    
    def select_gesture(self):
        gesture_selection = ''
        while gesture_selection not in range(1,6):
            try:
                gesture_selection = int(input(f'\nSelect your move: '))
                
            except ValueError: 
                print('Invalid Input')
                
        # while gesture_selection != range(1,6):
        #     print('Invalid')
        #     gesture_selection = input(f'\nSelect your move: ')

        gesture_selection = int(gesture_selection)
        gesture_index = gesture_selection - 1
        gesture = self.gestures[gesture_index]
        return gesture

    def get_name(self, player_name):
        self.name = input(f'\n{player_name} what is your name? ')
        print()

    def score_point(self):
        self.points += 1
        
#Try and Except