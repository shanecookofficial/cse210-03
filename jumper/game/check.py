class Check:
    def __init__(self):
        self.check = None
    
    def checkGuess(self, guess, word):
        for i in word:
            if guess == i:
                return True
        return False
