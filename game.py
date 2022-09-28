from player import Player
from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = self.multiplayer_or_AI()



    def display_greeting(self):
        print(f'\n')
        print('Welcome to rock paper scissors lizard spock')

    def run_game(self):
        pass

    def multiplayer_or_AI(self):
        selection = int(input('Play against \n [1] Friend \n[2] Computer?\n'))
        while selection != 1 and selection != 2:
            selection = int(input('Invalid, please enter 1 or 2: '))
        if selection == 1:
            self.player2 = Human()
        if selection == 2:
            self.player2 = AI()

        
