import pygame
import math

from vector_functions import lorentz_transformation
from constants import speed_of_light
from player import Player


class GameObject:
    def __init__(self, position, x_velocity, y_velocity, color):
        self.position = position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.color = color

    def render(self, window):
        shape_measured = self.get_shape_measured()
        shape_observed = self.get_shape_observed(player)
        shape_original = self.get_shape_original()
        color = (0, 0, 0)
        if self.color == "g1":
            color = (255, 244, 234)
        elif self.color == "o1":
            color = (155, 176, 255)
        elif self.color == "b1":
            color = (170, 191, 255)
        elif self.color == "a1":
            color = (202, 215, 255)
        elif self.color == "f1":
            color = (248, 247, 255)
        elif self.color == "k1":
            color = (255, 210, 161)
        elif self.color == "m1":
            color = (255, 204, 111)
        else:
            color = (255, 0, 0)
        for i in range(len(shape_measured)):
            new_tuple = (
                shape_measured[i][0] + self.position[0],
                shape_measured[i][1] + self.position[1],
            )
            shape_measured[i] = new_tuple

        for i in range(len(shape_original)):
            new_tuple = (
                shape_original[i][0] + self.position[0],
                shape_original[i][1] + self.position[1],
            )
            shape_original[i] = new_tuple

        pygame.draw.polygon(window, (255, 0, 0), shape_original, width=0)
        pygame.draw.polygon(window, (0, 255, 0), shape_observed, width=0)
        pygame.draw.polygon(window, color, shape_measured, width=0)


player = Player()


class Star(GameObject):
    def __init__(self, position, x_velocity, y_velocity, color):
        super().__init__(position, x_velocity, y_velocity, color)
        self.orgin_position = self.position
        self.photon_list = []
        self.lastknown = self.position
        self.color = color

    def get_shape_measured(self):
        return lorentz_transformation(
            player,
            self.position,
            self.get_shape_original(),
        )

    def get_shape_observed(self, frame):
        offset = self.get_shape_measured()

        observer_x, observer_y = frame.position
        photon_velocityx = speed_of_light * frame.x_velocity
        photon_velocity = speed_of_light * frame.y_velocity
        photon_velocity_magnitude = math.sqrt(photon_velocityx**2 + photon_velocity**2)

        observed_shape = []

        for i in offset:
            x = i[0] + self.position[0]
            y = i[1] + self.position[1]

            dx = x - observer_x
            dy = y - observer_y

            a = speed_of_light - photon_velocity_magnitude
            b = -2.0 * (dx * photon_velocityx + dy * photon_velocity)
            c = -(dx**2 + dy**2)

            discrimanent = b**2 - 4.0 * a * c
            if discrimanent < 0:
                discrimanent = 0
            time_of_emmission = (-b - math.sqrt(discrimanent)) / (2.0 * a)

            x_observed = x + photon_velocityx * time_of_emmission
            y_observed = y + photon_velocity * time_of_emmission

            observed_shape.append((x_observed, y_observed))
        return observed_shape

    def get_shape_original(self):
        return [
            (20, 20),
            (45, 0),
            (20, -20),
            (0, -45),
            (-20, -20),
            (-45, 0),
            (-20, 20),
            (0, 45),
        ]

    def update(self, frame):
        self.position = (
            self.position[0] + speed_of_light * frame.x_velocity,
            self.position[1] + speed_of_light * frame.y_velocity,
        )
        if frame.reset == True:
            self.position = self.orgin_position
