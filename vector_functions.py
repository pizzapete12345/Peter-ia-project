import math
import pygame


def rotates(point):
    vector=pygame.math.Vector2(point)
    return(vector.rotate(1))
def counter_rotates(points):
    vector=pygame.math.Vector2(points)
    return(vector.rotate(-1))