""" Code for game setup and call classes from other files to be used in the game"""
from game.displayPlayer import displayPlayer
from game.check import Check
from game.word import Word
import random


class Director:
    """This class will initiate and direct the flow of the jumper game.

    Attributes:

        play: boolean - tracks if the player wants to play again or not"""

    # Shane
    def __init__(self) -> None:
        self._play = True
        self._lives = 4
        self._displayPlayer = displayPlayer()
        self._check = Check()
        self._word = Word()
        self._guess = ""
        self._guesses = []

    # Shane

    def start_game(self):
        """
        Starts the game by running the main game loop.

        Args:
            self (Director): An instance of Director.
        """

        while self._play:
            self._displayPlayer.displayJumper()
            self._secret_word = self._word.pickWord()
            self.play()
            self.play_again()

    # Antonio
    def play(self):
        if not self._play:
            return

        while self._lives > 0:
            self._guess = input("Guess a letter [a-z]: ")

            while (not self._guess.isalpha()) or (len(self._guess) > 1) or (self._guess in self._guesses):
                self._guess = input("Guess a letter [a-z]: ")

            if not self._check.checkGuess(self._guess, self._secret_word):
                self._lives -= 1
                self._displayPlayer.displayUpdate()
            else:
                self._guesses.append(self._guess)
            for i in self._secret_word:
                if i in self._guesses:
                    print(i)
                else:
                    print("_")
            self._displayPlayer.displayJumper()

    # Shane

    # def play_again(self):
    #     """
    #     Asks the user if they want to play again.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     if not self._play:
    #         return

    #     elif self._lives == 0:
    #         answer = ""

    #         while (answer != "y" and answer != "n"):
    #             answer = input("Want to play again? [y/n] ").lower()

    #             if (answer != "n" and answer != "y"):
    #                 print("Please enter a \"y\" or a \"n\".")

    #         if answer == "n":
    #             print("\nGame over. You chose to stop playing.\n")
    #             self._play = False
    #         else:
    #             self._play = True

    #     else:
    #         return


"""Shane Cook and Antonio Saucedo are the authors of this document"""
