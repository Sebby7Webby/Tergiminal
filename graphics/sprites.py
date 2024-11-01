class Sprites:
    """
        # Sprites
        ## Blocks
        Blocks and Rectangles 
        ## Quadrants
        Sprites based on four quadrants
    """
    class Blocks:
        """
            f{n} = (block of shading density = n/4), only 4 through 1 inclusive
            
            l{n} and b{n} = (size = n/8), only 7 through 1 inclusive

            l = left aligned
            
            b = bottom alinged
        """
        # Full Blocks
        f4 = '\u2588'
        f3 = '\u2593'
        f2 = '\u2592'
        f1 = '\u2591'

        # Left aligned
        l7 = '\u2589'
        l6 = '\u258A'
        l5 = '\u258B'
        l4 = '\u258C'
        l3 = '\u258D'
        l2 = '\u258E'
        l1 = '\u258F'

        # Bottom aligned
        b7 = '\u2581'
        b6 = '\u2582'
        b5 = '\u2583'
        b4 = '\u2584'
        b3 = '\u2585'
        b2 = '\u2586'
        b1 = '\u2587'

    class Quadrants:
        """
        North = Top right = n

        East = Bottom Right = e

        South = Bottom Left = s

        West = Top Left = w

        q{dir} = block in quarter of dir

        arr{dir} = arrow in direcetion of dir

        dualns = quarters north and south filled

        dualew = quarters east and west filled
        """

        # Quarters
        qn = '\u259D'
        qe = '\u2597'
        qs = '\u2596'
        qw = '\u2598'

        # Arrows
        arrn = '\u259C'
        arre = '\u259F'
        arrs = '\u2599'
        arrw = '\u259B'

        # Diagonals
        dualns = '\u259E'
        dualew = '\u259A'



class Colour:
    def __init__(self, r: int = None, g: int = None, b: int = None, id: str = None):
        if id is None:
            if r is None or g is None or b is None or 0 > r or r > 255 or 0 > g or g > 255 or 0 > b or b > 255:
                raise ValueError("If no id is given r, g, b need values between 0 and 255")
            self.value = (r, g, b)
        else:
            match (id):
                case "RED":
                    self.value = (255, 0, 0)
                case "GREEN":
                    self.value = (0, 255, 0)
                case "BLUE":
                    self.value = (0, 0, 255)
                case "WHITE":
                    self.value = (255, 255, 255)
                case "BLACK":
                    self.value = (0, 0, 0)
                case "GREY":
                    self.value = (128, 128, 128)
                case _:
                    raise ValueError("Id uncrecognised")
    
    def set(self):
        print(f'\033[38;2;{self.value[0]};{self.value[1]};{self.value[2]}m', end="")
    
    def reset(self = None):
        print("\033[0m", end="")

    def __repr__(self):
        return str(self.value)


class Movements:
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)

class Pixel:
    def __init__(self, value, parent: 'Sprite' = None, colour: Colour = Colour(id="WHITE")):
        self.value = value
        self.parent = None
        if colour is None:
            self.colour = Colour(id="WHITE")
        else:
            self.colour = colour

        if parent is not None:
            self.parent = parent

    def display(self):
        self.colour.set()
        print(self.value, end="")

    def empty(self):
        self.colour = Colour(id="WHITE")
        self.parent = None
        self.value = ' '

    def paste(self):
        return Pixel(self.value, self.parent, self.colour)

class Sprite:
    def __init__(self, map: list[list[Pixel | None]] | list[list], pos: tuple[int], colour: Colour = Colour(id="WHITE"),):
        if isinstance(map[0][0], Pixel):
            for row in map:
                for pixel in row:
                    pixel.parent = self
            self.map = map
        else:
            self.map = [[Pixel(pixel, self, colour) for pixel in row] for row in map]
        self.pos = pos

    def moveBy(self, move: tuple[int]):
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def moveTo(self, coords: tuple[int]):
        self.pos = coords

    def reColour(self, colour: Colour, replace: Colour = None):
        if replace is None:
            for row in self.map:
                for pixel in row:
                    pixel.colour = colour
        else:
            for row in self.map:
                for pixel in row:
                    if pixel.colour.value == replace.value:
                        pixel.colour = colour
