class displayPlayer:

    def __init__(self):

        self.jumperDisplay = ["  ___", " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "", "^^^^^^^"]

    def displayUpdate(self):

        self.jumperDisplay.pop(0)

    def displayJumper(self):

        for i in self.jumperDisplay:
            print(i)