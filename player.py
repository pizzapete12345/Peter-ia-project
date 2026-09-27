import pygame
import math
from vector_functions import rotates, dampening
from constants import speed_of_light


class Player:
    def __init__(self):
        self.vertices = [(0, 30), (25, -25),(0,-15), (-25, -25)]

        self.p1 = (0, 25)
        self.p2 = (25, -25)
        self.p3 = (-25, -25)

        self.color = (169, 169, 169)

        self.x_velocity = 0
        self.y_velocity = 0
        self.position = (640, 360)

        self.angle = 3.1415

        self.reset = False

    def render(self, window):
        self.reset = False
        withpos = []
        for i in self.vertices:
            withpos.append((i[0] + self.position[0], i[1] + self.position[1]))
        pygame.draw.polygon(
            window,
            self.color,
            withpos,
            width=0,
        )

    def movement(self):
        key_pressed = pygame.key.get_pressed()
        acceleration = 0.01 * (
            1 - (self.x_velocity**2 + self.y_velocity**2) / speed_of_light**2
        )

        if math.sqrt(self.x_velocity**2 + self.y_velocity**2) > 0.99:
            dampening(self, 0.01)

        if key_pressed[pygame.K_w]:
            self.y_velocity = self.y_velocity + acceleration * math.cos(self.angle)
            self.x_velocity = self.x_velocity - acceleration * math.sin(self.angle)

        if key_pressed[pygame.K_s]:
            self.y_velocity = self.y_velocity - acceleration * math.cos(self.angle)
            self.x_velocity = self.x_velocity + acceleration * math.sin(self.angle)
        if key_pressed[pygame.K_d]:
            self.x_velocity = self.x_velocity - acceleration * math.cos(self.angle)
            self.y_velocity = self.y_velocity - acceleration * math.sin(self.angle)
        if key_pressed[pygame.K_a]:
            self.x_velocity = self.x_velocity + acceleration * math.cos(self.angle)
            self.y_velocity = self.y_velocity + acceleration * math.sin(self.angle)
        if key_pressed[pygame.K_1]:
            self.y_velocity = 0
            self.x_velocity = 0
        if key_pressed[pygame.K_2]:
            self.y_velocity = 0.25 * math.cos(self.angle)
            self.x_velocity = -0.25 * math.sin(self.angle)
        if key_pressed[pygame.K_3]:
            self.y_velocity = 0.5 * math.cos(self.angle)
            self.x_velocity = -0.5 * math.sin(self.angle)
        if key_pressed[pygame.K_4]:
            self.y_velocity = 0.75 * math.cos(self.angle)
            self.x_velocity = -0.75 * math.sin(self.angle)
        if key_pressed[pygame.K_5]:
            self.y_velocity = 0.99 * math.cos(self.angle)
            self.x_velocity = -0.99 * math.sin(self.angle)

        if key_pressed[pygame.K_e]:
            self.vertices = rotates(self.vertices, 1)

            self.angle = self.angle + 0.0175

        if key_pressed[pygame.K_q]:
            self.vertices = rotates(self.vertices, -1)

            self.angle = self.angle - 0.0175

        if key_pressed[pygame.K_b]:
            dampening(self, 0.01)

        if key_pressed[pygame.K_r]:
            self.reset = True
            self.x_velocity = 0
            self.y_velocity = 0
