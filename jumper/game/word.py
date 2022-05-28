import random

class Word:
    """This class will check if a guess is correct or not.

    Attributes:

        library: list - stores a list of words for the player to guess from."""

    def __init__(self) -> None:
        self.library = [
"flamingo",
"boutique",
"hurricane",
"freezing",
"parachute",
"escalator",
"taco",
"salad",
"plane",
"technology",
"door",
"dress",
"pineapple",
"joy",
"conditioner",
"hymn",
"laugh",
"guess",
"switch",
"paper"]
    
    def pickWord(self):

        return random.choice(self.library)