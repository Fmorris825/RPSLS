from lizard import Lizard
from scissors import Scissors
from rock import Rock
from paper import Paper

class Spock:
    def __init__(self):
        self.name = 'Spock'
        self.loses_to = [Lizard.name, Paper.name]
        self.wins_to = [Scissors.name, Rock.name]

#beats rock and scissors
#loses to lizard and paper