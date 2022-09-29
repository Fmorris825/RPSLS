from player import Player


class Human(Player):
    def __init__(self):
        self.name = ''
        super().__init__()

    def select_gesture(self):
        return super().select_gesture(self.name)

    def get_name(self):
        return super().get_name()

