from paper import Paper
from rock import Rock
from scissors import Scissors
from spock import Spock
from paper import Paper

class Lizard:
    def __init__(self):
        self.name = 'Lizard'
        self.loses_to = [Rock.name, Scissors.name]
        self.wins_to = [Spock.name, Paper.name]

#beats Spock and paper
#beat by rock and scissors
