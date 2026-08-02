import pygame

class GameObject:
    def __init__(self,position,x_velocity,y_velocity):
        self.position=position
        self.x_velocity=x_velocity
        self.y_velocity=y_velocity
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
        self.x_velocity=0
        self.y_velocity=0
        self.position=(0,0)
        self.dampening=0
    def get_shape(self):
        return [(300, 100), (150, 300), (450, 300)]
    def movement(self):
        key_pressed=pygame.key.get_pressed()

        if key_pressed[pygame.K_w]:
            self.y_velocity=self.y_velocity-0.1
        if key_pressed[pygame.K_s]:
            self.y_velocity=self.y_velocity+0.1
        if key_pressed[pygame.K_d]:
            self.x_velocity=self.x_velocity+0.1
        if key_pressed[pygame.K_a]:
            self.x_velocity=self.x_velocity-0.1

        if self.x_velocity>0:
            self.x_velocity=self.x_velocity-self.dampening
        elif self.x_velocity<0:
            self.x_velocity=self.x_velocity+self.dampening
        if self.y_velocity>0:
            self.y_velocity=self.y_velocity-self.dampening
        elif self.y_velocity<0:
            self.y_velocity=self.y_velocity+self.dampening

        if self.x_velocity<0.05 and self.x_velocity>-0.05:
            self.x_velocity=0
        if self.y_velocity<0.05 and self.y_velocity>-0.05:
            self.y_velocity=0
            
        
        

class Star(GameObject):

    def get_shape(self):
        return [(100, 100), (0, 100), (100, 0)]
    def update(self,frame):
        self.position=(self.position[0]+frame.x_velocity,self.position[1]+frame.y_velocity)
