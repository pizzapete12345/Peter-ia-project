import pygame
import math

from vector_functions import lorentz_transformation,translate
from constants import speed_of_light
from player import Player


class GameObject:
    def __init__(self, position, star_type):
        self.position = position
        self.star_type = star_type
        if self.star_type == "g1":
            self.color = (255, 244, 234)
        elif self.star_type == "o1":
            self.color = (155, 176, 255)
        elif self.star_type == "b1":
            self.color = (170, 191, 255)
        elif self.star_type == "a1":
            self.color = (202, 215, 255)
        elif self.star_type == "f1":
            self.color = (248, 247, 255)
        elif self.star_type == "k1":
            self.color = (255, 210, 161)
        elif self.star_type == "m1":
            self.color = (255, 204, 111)
        else:
            self.color = (255, 0, 0)

    def render(self, window):
        shape_measured = translate(self.get_shape_measured(),self.position)
        shape_observed = self.get_shape_observed(player)
        shape_original = translate(self.get_shape_original(),self.position)


        pygame.draw.polygon(window, (255, 0, 0), shape_original, width=0)
        pygame.draw.polygon(window, (0, 255, 0), shape_observed, width=0)
        pygame.draw.polygon(window, self.color, shape_measured, width=0)


player = Player()


class Star(GameObject):
    def __init__(self, position, star_type):
        super().__init__(position, star_type)
        self.orgin_position = self.position
        self.lastknown = self.position

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
