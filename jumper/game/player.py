# Class player, it represents the player of the game

class Player:
    
    # Constructor for the class Player
    # It initializes the following private class attributes
    # life: integer - it holds the life of the player
    # parachuteLife: list of strings - it holds the parachute of the player, another representation for the life of the player
    # letterChosen: a character - it holds the letter chosen by the player, this will be used to guess
    def __init__(self):
        self._life = 4
        self._parachuteLife = ["  ___", " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "", "^^^^^^^"]
        self._letterChosen = ""

    # Function for returning the private attribute life
    def getLife(self):
        return self._life

    # Function for returning the private attribute parachuteLife
    def getParachuteLife(self):
        return self._parachuteLife 

    # Function for returning the private attribute letterChosen
    def getLetterChosen(self):
        return self._letterChosen

    # Function to update the life of the player
    def updateLife(self, newLife):
        self._life = newLife

    # Function to update the parachuteLife attribute
    #def updateParachuteLife(self):
    #    pass

    # Function to update the letterChosen attribute
    def updateLetterChosen(self, newLetter):
        self._letterChosen = newLetter

# Examples of how to use this class
def main():
    # Create and instance of the Player class
    player = Player()

    # Getting private attribute life, it represents the player's life
    life = player.getLife()
    print(f"life: {life}")

    # Getting private attribute parachuteLife, another representation of the player's life
    parachute = player.getParachuteLife()
    for elem in parachute:
        print(elem)
    
    # Updating the new player's life
    player.updateLife(life-1)

    # Getting private attribute life, it represents the player's life
    life = player.getLife()
    print(f"life: {life}")

    # Removing the first element from the parachuteLife attribute, 
    # because it is a list of strings, it will automatically be updated 
    parachute.pop(0)
    for elem in parachute:
        print(elem)

    # Updating the new player's life
    player.updateLife(life-1)

    # Getting private attribute life, it represents the player's life
    life = player.getLife()
    print(f"life: {life}")

    # Removing the first element from the parachuteLife attribute, 
    # because it is a list of strings, it will automatically be updated
    parachute.pop(0)
    # Getting attribute parachuteLife to prove that it is updated
    for elem in player.getParachuteLife():
        print(elem)

    # Updating the new player's life
    player.updateLife(life-1)

    # Getting private attribute life, it represents the player's life
    life = player.getLife()
    print(f"life: {life}")

    # Removing the first element from the parachuteLife attribute, 
    # because it is a list of strings, it will automatically be updated
    parachute.pop(0)
    # Getting attribute parachuteLife to prove that it is updated
    for elem in player.getParachuteLife():
        print(elem)

if __name__ == "__main__":
    main()