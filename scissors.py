from lizard import Lizard
from paper import Paper
from rock import Rock
from spock import Spock


class Scissors:
    def __init__(self):
        self.name = 'Scissors'
        self.loses_to = [Spock.name, Rock.name]
        self.wins_to = [Paper.name, Lizard.name]

# Scissors beats paper and lizard
# beat by Spock and Rock