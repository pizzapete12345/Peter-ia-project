import pygame

class GameObject:
    def __init__(self,position):
        self.position=position
    def render(self,window):
        shape=self.get_shape()
        for i in range(len(shape)):
            new_tuple=(
            shape[i][0]+self.position[0],
            shape[i][1]+self.position[1]
            )
            shape[i]=new_tuple


        pygame.draw.polygon(window,(255,0,0),shape,width=0)

class Player(GameObject):
    def __init__(self):
        self.position=(0,0)
    def get_shape(self):
        return [(300, 100), (150, 300), (450, 300)]

class Star(GameObject):

    def get_shape(self):
        return [(10, 100), (100, 300), (450, 300)]
    def update(self):
        self.position=(self.position[0]+1,self.position[1])