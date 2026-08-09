import pygame
import math

from vector_functions import rotates 
from vector_functions import counter_rotates,dampening,lorentz_transformation
from constants import speed_of_light

class GameObject:
    def __init__(self,position,x_velocity,y_velocity,color):
        self.position=position
        self.x_velocity=x_velocity
        self.y_velocity=y_velocity
        self.color=color
    def render(self,window):
        shape=self.get_shape()
        color=(0,0,0)
        if self.color=="g1":
            color=(255, 244, 234)
        elif self.color=="o1":
            color=(155, 176, 255)
        elif self.color=="b1":
            color=(170, 191, 255)
        elif self.color=="a1":
            color=(202, 215, 255)
        elif self.color=="f1":
            color=(248, 247, 255)
        elif self.color=="k1":
            color=(255, 210, 161)
        elif self.color=="m1":
            color=(255, 204, 111)
        else:
            color=(255,0,0)
        for i in range(len(shape)):
            new_tuple=(
            shape[i][0]+self.position[0],
            shape[i][1]+self.position[1]
            )
            shape[i]=new_tuple


        pygame.draw.polygon(window,color,shape,width=0)

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
        acceleration=0.01*(1-(self.x_velocity**2+self.y_velocity**2)/speed_of_light**2)
        print("acceleration =",acceleration)

        if math.sqrt(self.x_velocity**2+self.y_velocity**2)>0.99:
            dampening(self,0.01)


        if key_pressed[pygame.K_w]:
            self.y_velocity=self.y_velocity+acceleration*math.cos(self.angle)
            self.x_velocity=self.x_velocity-acceleration*math.sin(self.angle)

        if key_pressed[pygame.K_s]:
            self.y_velocity=self.y_velocity-acceleration*math.cos(self.angle)
            self.x_velocity=self.x_velocity+acceleration*math.sin(self.angle)
        if key_pressed[pygame.K_d]:
            self.x_velocity=self.x_velocity-acceleration*math.cos(self.angle)
            self.y_velocity=self.y_velocity-acceleration*math.sin(self.angle)
        if key_pressed[pygame.K_a]:
                self.x_velocity=self.x_velocity+acceleration*math.cos(self.angle)
                self.y_velocity=self.y_velocity+acceleration*math.sin(self.angle)
        if key_pressed[pygame.K_1]:
            self.y_velocity=0
            self.x_velocity=0
        if key_pressed[pygame.K_2]:
            self.y_velocity=0.25*math.cos(self.angle)
            self.x_velocity=-0.25*math.sin(self.angle)
        if key_pressed[pygame.K_3]:
            self.y_velocity=0.5*math.cos(self.angle)
            self.x_velocity=-0.5*math.sin(self.angle)
        if key_pressed[pygame.K_4]:
            self.y_velocity=0.75*math.cos(self.angle)
            self.x_velocity=-0.75*math.sin(self.angle)
        if key_pressed[pygame.K_5]:
            self.y_velocity=0.99*math.cos(self.angle)
            self.x_velocity=-0.99*math.sin(self.angle)

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
            dampening(self,0.1)

        if key_pressed[pygame.K_r]:
            self.reset=True
            self.x_velocity=0
            self.y_velocity=0

            
player=Player()        
        

class Star(GameObject):
    def __init__(self, position, x_velocity, y_velocity, color):
        super().__init__(position, x_velocity, y_velocity,color)
        self.orgin_position=self.position
        self.color=color
        

    def get_shape(self):
        
        return lorentz_transformation(player,self,[(20, 20),(45,0), (20, -20),(0,-45) ,(-20, -20),(-45,0),(-20, 20),(0,45)])
    def update(self,frame):
        self.position=(self.position[0]+speed_of_light*frame.x_velocity,self.position[1]+speed_of_light*frame.y_velocity)
        if frame.reset==True:
            self.position=self.orgin_position

