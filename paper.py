from lizard import Lizard
from rock import Rock
from scissors import Scissors
from spock import Spock


class Paper:
    def __init__(self):
        self.name = 'Paper'
        self.loses_to = [Lizard.name, Scissors.name]
        self.wins_to = [Rock.name, Spock.name]


#paper beats rock and Spock
#beat by lizard and scissors