import pygame
import math

from vector_functions import rotates 
from vector_functions import counter_rotates,dampening

class GameObject:
    def __init__(self,position,x_velocity,y_velocity,color):
        self.position=position
        self.x_velocity=x_velocity
        self.y_velocity=y_velocity
        self.color=color
    def render(self,window):
        shape=self.get_shape()
        for i in range(len(shape)):
            new_tuple=(
            shape[i][0]+self.position[0],
            shape[i][1]+self.position[1]
            )
            shape[i]=new_tuple


        pygame.draw.polygon(window,self.color,shape,width=0)

class Player(GameObject):
    def __init__(self):

        self.p1=(0,25)
        self.p2=(25,-25)
        self.p3=(-25,-25)

        self.color=(255,0,0)

        self.x_velocity=0
        self.y_velocity=0
        self.position=(640,360)

        self.angle=3.1415

        self.reset=False

    def get_shape(self):
        self.reset=False
        return [self.p1, self.p2, self.p3]
        
    
    def movement(self):
        key_pressed=pygame.key.get_pressed()

        if key_pressed[pygame.K_w]:
            self.y_velocity=self.y_velocity+0.1*math.cos(self.angle)
            self.x_velocity=self.x_velocity-0.1*math.sin(self.angle)

        if key_pressed[pygame.K_s]:
            self.y_velocity=self.y_velocity-0.1*math.cos(self.angle)
            self.x_velocity=self.x_velocity+0.1*math.sin(self.angle)
        if key_pressed[pygame.K_d]:
            self.x_velocity=self.x_velocity-0.1*math.cos(self.angle)
            self.y_velocity=self.y_velocity-0.1*math.sin(self.angle)
        if key_pressed[pygame.K_a]:
            self.x_velocity=self.x_velocity+0.1*math.cos(self.angle)
            self.y_velocity=self.y_velocity+0.1*math.sin(self.angle)

        if key_pressed[pygame.K_e]:
            self.p1=rotates(self.p1)
            self.p2=rotates(self.p2)
            self.p3=rotates(self.p3)

            self.angle=self.angle+0.0175

        if key_pressed[pygame.K_q]:
            self.p1=counter_rotates(self.p1)
            self.p2=counter_rotates(self.p2)
            self.p3=counter_rotates(self.p3)

            self.angle=self.angle-0.0175

        if key_pressed[pygame.K_b]:
            dampening(self,0.025)

        if key_pressed[pygame.K_r]:
            self.reset=True
            self.x_velocity=0
            self.y_velocity=0

            
        
        

class Star(GameObject):
    def __init__(self, position, x_velocity, y_velocity, color):
        super().__init__(position, x_velocity, y_velocity, color)
        self.orgin_position=self.position

    def get_shape(self):
        return [(20, 20),(45,0), (20, -20),(0,-45) ,(-20, -20),(-45,0),(-20, 20),(0,45)]
    def update(self,frame):
        self.position=(self.position[0]+frame.x_velocity,self.position[1]+frame.y_velocity)
        if frame.reset==True:
            self.position=self.orgin_position

