from .display import Display
from .sprites import Colour, Pixel, Sprites

def drawLine(coord1: tuple[int], coord2: tuple[int], display: Display, colour: Colour):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]

    dx = x2-x1
    dy = y2-y1
    D = 2*dy - dx
    y = y1

    for x in range(x1, x2):
        display.display[x][y] = Pixel(Sprites.Blocks.f4, colour=colour)
        if D > 0:
            y = y+1
            D = D - 2*dx
        D = D + 2*dy
