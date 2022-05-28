""" Code for game setup and call classes from other files to be used in the game"""
from game.displayPlayer import displayPlayer
from game.check import Check
from game.word import Word
import sys


class Director:
    """This class will initiate and direct the flow of the jumper game.

    Attributes:

        play: boolean - tracks if the player wants to play or not.
        lives: integer - tracks player lives.
        displayPlayer: list - tracks jumper visuals.
        check: boolean - tracks if a guess is correct or not.
        word: string - stores the word to be guessed by player.
        guess: string - stores players guess.
        guesses: list - stores a list of player guesses.
        guessedCorrect - tracks the number of letters guessed.
        playAgain: string - stores the players choice of playing again or not."""

    # Shane & Antonio
    def __init__(self) -> None:
        self._play = True
        self._lives = 4
        self._displayPlayer = displayPlayer()
        self._check = Check()
        self._word = Word()
        self._guess = ""
        self._guesses = []
        self._guessedCorrect = 0
        self._playAgain = ""

    # Shane
    def start_game(self):
        """
        Starts the game by running the main game loop.

        Args:
            self (Director): An instance of Director.
        """

        while self._play:
            self._secret_word = self._word.pickWord()

            for i in self._secret_word:
                print("_ ", end="")
            print("\n")
            self._displayPlayer.displayJumper()
            self.play()
            self.play_again()

    # Antonio
    def play(self):
        """
        Runs the game until the word has been guessed or player has no more lives.

        Args:
            self (Director): An instance of Director.
        """

        while (self._lives > 0):
            self._guess = input("Guess a letter [a-z]: ")

            while (not self._guess.isalpha()) or (len(self._guess) > 1) or (self._guess in self._guesses):
                self._guess = input("Guess a letter [a-z]: ")

            if not self._check.checkGuess(self._guess, self._secret_word):
                self._lives -= 1
                self._displayPlayer.displayUpdate(self._lives)
            else:
                self._guesses.append(self._guess)

            for i in self._secret_word:
                if i in self._guesses:
                    print(i + " ", end="")
                else:
                    print("_ ", end="")
            self._guessedCorrect = 0
            for char in self._secret_word:
                if char in self._guesses:
                    self._guessedCorrect += 1
            if self._guessedCorrect == len(self._secret_word):
                self._lives = 0
            print("\n")
            self._displayPlayer.displayJumper()

    # Shane & Antonio
    def play_again(self):
        """
        Asks the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        self._play_again = input("Do ya wanna play again? [y/n] ")

        while ((not self._play_again.isalpha()) or (self._play_again.lower() not in ("y", "n"))):
            self._play_again = input("Do ya wanna play again? [y/n] ")

        if (self._play_again.lower() == "n"):
            print("\nThank you for playing!")
            sys.exit()
        else:
            self._lives = 4
            self._displayPlayer = displayPlayer()
            self._guesses = []


"""Shane Cook and Antonio Saucedo are the authors of this document"""
