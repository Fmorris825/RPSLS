

class Player:
    def __init__(self):
        self.name = ''
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.points = 0
    
    def select_gesture(self):
        gesture_selection = ''
        while_loop_count = 0
        while gesture_selection not in range(1,6):
            while_loop_count += 1
            if while_loop_count > 1:
                print('\nPay attention to directions.')
            try:
                gesture_selection = int(input(f'Select a number 1-5: '))
                
            except ValueError: 
                pass

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