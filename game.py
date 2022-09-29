from re import T
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
        player1_wins = 0
        player2_wins = 0
        while player1_wins < 2 and player2_wins < 2:
            player1_gesture = self.player1.select_gesture()
            player2_gesture = self.player2.select_gesture()
            while player1_gesture == player2_gesture:
                print('Tie! Try again!')
                player1_gesture = self.player1.select_gesture()
                player2_gesture = self.player2.select_gesture()
            player1_victory = self.decide_winner(player1_gesture, player2_gesture)
            
            if player1_victory:
                player1_wins += 1
            else:
                player2_wins += 1


    def get_name(self):
        self.player1.get_name()
        self.player2.get_name()

    def decide_winner(self, player1_gesture, player2_gesture):
        player1_victory = False
        if player1_gesture == 'Rock':
            if player2_gesture == 'Scissors' or player2_gesture == 'Lizard':
                player1_victory = True
        if player1_gesture == 'Paper':
            if player2_gesture == 'Spock' or player2_gesture == 'Rock':
                player1_victory = True
        if player1_gesture == 'Scissors':
            if player2_gesture == 'Paper' or player2_gesture == 'Lizard':
                player1_victory = True
        if player1_gesture == 'Lizard':
            if player2_gesture == 'Spock' or player2_gesture == 'Paper':
                player1_victory = True
        if player1_gesture == 'Spock':
            if player2_gesture == 'Rock' or player2_gesture == 'Scissors':
                player1_victory = True
        return player1_victory
                


    def run_game(self):
        # self.display_greeting()
        self.multiplayer_or_ai()
        self.get_name()
        # self.display_rules()
        self.run_match()
        