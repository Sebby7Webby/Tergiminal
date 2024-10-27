import graphics.display as ds
import graphics.sprites as sp
import graphics.draw as dr
from time import sleep

display = ds.Display()
map = [
    [sp.Pixel(sp.Sprites.Blocks.f4, colour=sp.Colour(255, 0, 0)), sp.Pixel(sp.Sprites.Blocks.f4, colour=sp.Colour(0, 255, 0))],
    [sp.Pixel(sp.Sprites.Blocks.f4, colour=sp.Colour(0, 0, 255)), sp.Pixel(sp.Sprites.Blocks.f4, colour=sp.Colour(255, 175, 0))]
]
player = sp.Sprite(map, (3, 5))

while True:
    sleep(0.01)
    player.moveBy(sp.Movements.right)
    
    display.plot(player)
    display.update()


