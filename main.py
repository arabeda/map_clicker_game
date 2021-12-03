import numpy as np
import pygame
import cv2

matrix = []

def slicer():
    background = cv2.imread('background.png')
    y = background.shape[0]
    x = background.shape[1]
    for i in range(0, int(y/25)):
        for j in range(0, int(x/25)):
            temp = Cell(25*i, 25*j)
            matrix.append(temp)
    return 0

class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.color = color

    def __str__(self):
        return "{} {}".format(self.x, self.y)

if __name__ == '__main__':
    slicer()
    [ print(str(x)) for x in matrix ]
