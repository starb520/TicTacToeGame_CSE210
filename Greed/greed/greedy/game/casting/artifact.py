from game.casting.actor import Actor
from game.shared.point import Point

class Artifact(Actor):
    '''Create an instance of an artificat.'''
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
    def __init__(self):
        super().__init__()
        # self._position = Point(0, 0)
        self._message = " "

    
    def get_message(self):
        return (self._message)

    
    def set_message(self, message):
        self._message = message

