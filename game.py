from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = ''

    def display_greeting(self):
        print(f'\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(f'$$$$$ Welcome to ROCK PAPER SCISSORS LIZARD SPOCK $$$$$$')
        print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

    def multiplayer_or_ai(self):
        print(f'What game mode do you want to play? ')
        selection = int(input('\n[1] Single \n[2] Multiplayer\n\n'))
        while selection != 1 and selection != 2:
            selection = int(input('Invalid, please enter 1 or 2: '))
        if selection == 1:
            self.player2 = AI()
        if selection == 2:
            self.player2 = Human()

    def display_rules(self):
        print(f'\n')
        print(f'Rules: \nFirst to win 2 rounds wins the match! \n')
        print('Rock crushes Scissors')
        print('Scissors cut Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print(f'\n')

    def run_match(self):
        player1_gesture = self.player1.select_gesture()
        player2_gesture = self.player2.select_gesture()
        self.decide_winner(player1_gesture, player2_gesture)

    def get_name(self):
        self.player1.get_name()
        self.player2.get_name()

    def decide_winner(self, player1_gesture, player2_gesture):
        player1_victory = False
        if player1_gesture == 'Rock':
            if player2_gesture == 'Scissors' or 'Lizard':
                player1_victory = True
                


    def run_game(self):
        self.display_greeting()
        self.multiplayer_or_ai()
        self.get_name()
        self.display_rules()
        self.run_match()
        