""" Code for game setup and call classes from other files to be used in the game"""
from player import player
from puzzle import puzzle
from terminal_service import terminal_services


class Director():
    """This class will initiate and direct the flow of the jumper game.

    Attributes:
        word: string - stores the word to guess
        displayPlayer: string - stores string of characters used to display jumper character
        guess: string - stores the user word guess
        lives: integer - stores number of lives remaining"""

    # Shane
    def __init__(self) -> None:
        self.guess = ""
        self.lives = 5

    # Shane
    def start_game(self):

        while self.lives > 0:
            pass

    # Antonio
    def get_inputs():
        pass

    # Antonio
    def do_outputs():
        pass


"""Shane Cook and Antonio Saucedo are the authors of this document"""
