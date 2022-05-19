""" Code for game setup and call classes from other files to be used in the game"""
from player import player
from puzzle import puzzle
from terminal_service import terminal_services

class Director():

    #Shane
    def __init__(self) -> None:
        self.guess = ""
        self.lives = 5
        
    #Shane
    def start_game(self):
        
        while self.lives > 0:
            pass

    def get_inputs():
        pass

    def do_outputs():
        pass

"""
Shane Cook and Antonio Saucedo are the authors of this document
"""