class displayPlayer:
    """This class will track the jumper game visuals.

    Attributes:

        jumperDisplay: list - stores the jumper visuals."""

    def __init__(self):

        self.jumperDisplay = ["  ___", " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "", "^^^^^^^"]

    def displayUpdate(self, lives):

        self.jumperDisplay.pop(0)

        if lives == 0:
            self.jumperDisplay[0] = "   x"

    def displayJumper(self):

        for i in self.jumperDisplay:
            print(i)