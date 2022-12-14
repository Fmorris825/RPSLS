import time
from time import sleep
from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = 'Player 2'
        self.rules = ['Rules:', 'First to win 2 rounds wins the match!','Paper covers Rock', 'Rock crushes Lizard','Lizard poisons Spock', 'Spock smashes Scissors',
        'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock','Spock vaporizes Rock']

    def display_greeting(self):
        print(f'\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(f'$$$$$ Welcome to ROCK PAPER SCISSORS LIZARD SPOCK $$$$$$')
        print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

    def multiplayer_or_ai(self):
        print(f'What game mode do you want to play? \n\n[1] Single \n[2] Multiplayer')
        selection = input('\nSelect 1 or 2: ')
        
        while selection != '1' and selection != '2':
            selection = input('\nPay attention to directions.\nSelect 1 or 2: ')
        if selection == '1':
            self.player2 = AI()
        if selection == '2':
            self.player2 = Human()


    def display_rules(self):
        for rule in self.rules:
            print(rule)
            sleep(.3)
        print()

    def run_match(self):
        self.player1_wins = 0
        self.player2_wins = 0
        while self.player1_wins < 2 and self.player2_wins < 2:
            sleep(1)
            self.display_gestures()
            sleep(1)
            player1_gesture = self.player1.select_gesture()
            player2_gesture = self.player2.select_gesture()
            while player1_gesture == player2_gesture:
                for gesture in self.player1.gestures:
                    print()
                    print(f'{gesture}!')
                    sleep(.3)
                print(f'\nTie! Try again!\n')
                self.display_gestures()
                player1_gesture = self.player1.select_gesture()
                player2_gesture = self.player2.select_gesture()

            print()
            for gesture in self.player1.gestures:
                print(f'{gesture}!')
                sleep(.3)
                print()
            
            player1_victory = self.decide_winner(player1_gesture, player2_gesture)

            if player1_victory:
                self.player1_wins += 1
            else:
                self.player2_wins += 1
            
            winner_bracket = "loses to"
            if player1_victory:
                winner_bracket = "beats"
            
            print(f'{self.player1.name}\'s {player1_gesture} {winner_bracket} {self.player2.name}\'s {player2_gesture}')
            print(f'{self.player1.name} : {self.player1_wins} | {self.player2.name} : {self.player2_wins}\n')

    def display_winner(self):
        if self.player1_wins == 2:
            print(f'{self.player1.name} wins!!')
        if self.player2_wins == 2:
            print(f'{self.player2.name} wins!!')


    def get_name(self):
        self.player1.get_name('Player 1')
        self.player2.get_name('Player 2')
        print(f'{self.player1.name} vs {self.player2.name}!')

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
                
    def display_gestures(self):
        i = 0
        for gesture in self.player1.gestures:
            i += 1
            print(f'[{i}] {gesture}')
        print()


    def run_game(self):
        self.display_greeting()
        self.multiplayer_or_ai()
        self.get_name()
        self.display_rules()
        self.run_match()
        self.display_winner()
        