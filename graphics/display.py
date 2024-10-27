from .sprites import Colour, Sprite, Pixel

class Display:
    def __init__(self, w=100, h=25):
        self.w = w
        self.h = h
        # index into using Display.display[x][y]
        self.display = [[Pixel(' ') for _ in range(h)] for _ in range(w)]

    def plot(self, sprite: Sprite):
        for row in self.display:
            for tile in row:
                if tile.parent is sprite:
                    print("FOUND")
                    tile.empty()

        pos = sprite.pos

        for i, row in enumerate(sprite.map):
            for j, tile in enumerate(row):
                if 0 < pos[0]+j < self.w and 0 < pos[1]+i < self.h:
                    self.display[pos[0]+j][pos[1]+i] = tile.paste()

    def reset(self):
        for row in self.display:
            for pixel in row:
                pixel.empty()
    
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
        self.reset()


