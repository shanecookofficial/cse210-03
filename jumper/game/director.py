""" Code for game setup and call classes from other files to be used in the game"""
from game.displayPlayer import displayPlayer
from game.check import Check
from game.word import Word
import sys


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
                    print(i + " ", end="")
                else:
                    print("_ ", end="")
            print("\n")
            self._displayPlayer.displayJumper()

    #Shane

    def play_again(self):
        """
        Asks the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """

        


"""Shane Cook and Antonio Saucedo are the authors of this document"""
