##imports the director class so the Puzzle class is a child class of the Director class
from director import Director
""" Game word and value generator """


class Puzzle(Director):
     def __init__(self) -> None:
        self.word_choice = ''
        self.hidden_word = ''
        self.temp_word = ''
    """This class will choose a random word from a list and the value of that word and send it to the director to use

    Attributes:
        words: list - stores list of words to pick from"""
    def words(self):
        words = []
        with open('cse210-03/jumper/game/word_list.txt','r') as w:
            words = w.readlines()
        self.word_choice = word_list[random.randint(0,20)]
        self.word_choice = self.word_choice[:-1]
        self.temp_word = self.word_choice
        """value: integer - stores word value
        
     Cross references if the user input is in the word_choice
    Assigns a self.hidden_word to a new hidden word based on correct guess
    Args: input = one letter string from user
    Returns a boolean: True for correct guess, False for incorrect
    """
    def check_input(self, letter):
        replace_dash = True
        correct_guess = False
        if letter in self.temp_word:
            while replace_dash:
                index = self.temp_word.find(letter)
                if index != -1:
                    self.hidden_word = self.hidden_word[:index] + letter + self.hidden_word[index + 1:]
                    self.temp_word = self.temp_word[:index] + "-" + self.temp_word[index + 1:]
                else:
                    replace_dash = False
            correct_guess = True
        return correct_guess
    
        """pickedWord: string - stores the picked word from the list"""
     """
    Checks to see if word_choice is guessed 
    Returns Boolean: True for a win, False for a continue
    """
    def check_complete(self):
        word_complete = False
        if self.word_choice == self.hidden_word:
            word_complete = True
        return word_complete

        
    """
    Creates and returns a hidden word from the word choice.
    Hidden word will be a string of "-" with the length of the word choice.
    NOTE: ONLY WILL CREATE HIDDEN WORD. IF USED TO UPDATE THIS WILL NULLIFY GUESSES
    input: word = the word choice
    """
    def set_hidden_word(self, word):    
        hidden_word = ""

        for i in range(len(word)):
            hidden_word += "-"
        self.hidden_word = hidden_word
    pass
