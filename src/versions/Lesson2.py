from matplotlib import pyplot as plt
from random import *
import numpy as np


class Coord_table:
    def __init__(self) -> None:
        self.side = 2

    def make_square(self, side=2, coords=(0, 0)):
        self.side = side
        plt.axes()
        rectangle = plt.Rectangle((-side/2,-side/2), side, side, fc='white',ec="black")
        plt.gca().add_patch(rectangle)
        plt.axis('scaled')

    def make_cyrcle(self, coords=(0, 0)):
        circle = plt.Circle(( 0, 0), self.side/2, fc='white',ec="black")
        plt.gca().add_patch(circle)
        plt.axis('scaled')

    def make_points(self, quantity=100):
        k = 200
        coordinates = []
        for i in range(quantity):
            coords = (randrange(-self.side/2 * k, self.side/2 * k), randrange(-self.side/2 * k, self.side/2 * k))
            coords = coords[0] / k, coords[1] / k
            x, y = coords
            coordinates.append([x, y])
        
        coordinates = num

        plt.scatter(coordinates)




    def show(self):
        plt.axis('scaled')
        plt.show()


table = Coord_table()
table.make_square()
table.make_cyrcle()
table.make_points()
table.show()