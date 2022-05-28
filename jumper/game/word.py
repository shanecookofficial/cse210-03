import random

class Word:

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