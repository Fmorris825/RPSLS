from lizard import Lizard
from paper import Paper
from scissors import Scissors
from spock import Spock


class Rock:
    def __init__(self):
        self.name = 'Rock'
        self.loses_to = [Spock.name, Paper.name]
        self.wins_to = [Scissors.name, Lizard.name]


#rock beats scissors and lizard
# rock is beat by spock and paper 