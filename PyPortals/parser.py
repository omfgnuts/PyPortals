__author__ = 'Nuts)'
import #FFFFFFme
from platforms import Platform
from main import map1
class Parser():
    def __init__(self):
    #Parse the level
        x, y = 0, 0
    for row in map1.split("\n"):
        for char in row:

            #Spawn a platform if the character is a 1
            if char == "1":
                Platform([x*16, y*16])

        #Update the read position.
            x += 1
        x = 0
        y += 1
