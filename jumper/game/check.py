class Check:
    """This class will check if a guess is correct or not.

    Attributes:

        check: boolean - tracks if a player guess is correct or not."""
    def __init__(self):
        self.check = None
    
    def checkGuess(self, guess, word):
        for i in word:
            if guess == i:
                return True
        return False
