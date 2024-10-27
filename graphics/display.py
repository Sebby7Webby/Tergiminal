from sprites import Sprite, Colour

class Pixel:
    def __init__(self, value, parent: Sprite = None, colour: Colour = None):
        self.value = value
        if colour is None:
            self.colour = Colour(id="WHITE")
        else:
            self.colour = colour

        if parent is not None:
            self.parent = parent
            self.colour = parent.colour

    def display(self):
        self.colour.set()
        print(self.value, end="")

class Display:
    def __init__(self, w=100, h=25):
        self.w = w
        self.h = h
        # index into using Display.display[x][y]
        self.display = [[Pixel(' ') for _ in range(h)] for _ in range(w)]
    
    def update(self):
        print("\033c", end="")
        print('\u250F' + ('\u2501' * self.w) + '\u2513')
        for y in range(self.h):
            print('\u2503', end="")

            for x in range(self.w):
                self.display[x][y].display()
                

            Colour.reset()
            print('\u2503')
        print('\u2517' + ('\u2501' * self.w) + '\u251B')

d = Display()
d.display[5][5] = Pixel('#', colour=Colour(id="RED"))
d.update()