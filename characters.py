import pygame

class Player:
    def __init__(self):
        pass


    def render(self,window):
        pygame.draw.polygon(window,(255,0,0),[(300, 100), (150, 300), (450, 300)],width=0)