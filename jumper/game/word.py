import random

class Word:
    """This class will check if a guess is correct or not.

    Attributes:

        library: list - stores a list of words for the player to guess from."""

    def __init__(self) -> None:
        self.library = [
"Flamingo",
"Boutique",
"Hurricane",
"Freezing",
"Parachute",
"Escalator",
"Taco",
"Salad",
"Plane",
"Technology",
"Door",
"Dress",
"Pineapple",
"Joy",
"Conditioner",
"Hymn",
"Laugh",
"Guess",
"Switch",
"Paper"]
    
    def pickWord(self):

        return random.choice(self.library)