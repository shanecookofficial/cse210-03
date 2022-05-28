""" Code for game setup and call classes from other files to be used in the game"""
from displayPlayer import displayPlayer
from check import Check
from word import Word
import random


class Director():
    """This class will initiate and direct the flow of the jumper game.

    Attributes:
        
        play: boolean - tracks if the player wants to play again or not"""

    # Shane
    def __init__(self) -> None:
        self.play = True
        self.lives = 4
        self._displayPlayer = displayPlayer()
        self._check = Check()
        self._word = Word()
        
        
    # Shane
    def start_game(self):
        """
        Starts the game by running the main game loop.

        Args:
            self (Director): An instance of Director.
        """

        while self.play:
            self._displayPlayer.displayJumper()
            self._secret_word = self._word.pickWord()
            self.get_inputs()
            self.do_outputs()
            self.play_again()

    # Antonio
    def get_inputs(self):
        if not self.play:
            return
        pass

    # Antonio
    def do_outputs(self):
        if not self.play:
            return
        pass
    
    #Shane
    def play_again(self):
        """
        Asks the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        if not self.play:
            return

        elif self.lives == 0:
            answer = ""

            while (answer != "y" and answer != "n"):
                answer = input("Want to play again? [y/n] ").lower()

                if (answer != "n" and answer !="y"):
                    print("Please enter a \"y\" or a \"n\".")

            if answer == "n":
                print ("\nGame over. You chose to stop playing.\n")
                self.play = False
            else:
                self.play = True

        else:
            return


"""Shane Cook and Antonio Saucedo are the authors of this document"""