import math
import pygame


def rotates(point):
    vector=pygame.math.Vector2(point)
    return(vector.rotate(1))
def counter_rotates(points):
    vector=pygame.math.Vector2(points)
    return(vector.rotate(-1))

def dampening(object,dampening_constant):
    if object.x_velocity>=0 and object.y_velocity>=0:
        velocity_angle=0.0
        if object.y_velocity==0:
            velocity_angle=0.0
        elif object.x_velocity==0:
            velocity_angle=90.0
        else:
            velocity_angle=math.atan(object.y_velocity/object.x_velocity)
        object.y_velocity=object.y_velocity-dampening_constant*math.sin(velocity_angle)
        object.x_velocity=object.x_velocity-dampening_constant*math.cos(velocity_angle)
    elif object.x_velocity<=0 and object.y_velocity<=0:
        velocity_angle=0.0
        if object.y_velocity==0:
            velocity_angle=0.0
        elif object.x_velocity==0:
            velocity_angle=90.0
        else:
            velocity_angle=math.atan(object.y_velocity/object.x_velocity)
        object.y_velocity=object.y_velocity+dampening_constant*math.sin(velocity_angle)
        object.x_velocity=object.x_velocity+dampening_constant*math.cos(velocity_angle)
    elif object.x_velocity>=0 and object.y_velocity<=0:
        velocity_angle=0.0
        if object.y_velocity==0:
            velocity_angle=0.0
        elif object.x_velocity==0:
            velocity_angle=90.0
        else:
            velocity_angle=math.atan(object.y_velocity/object.x_velocity)
        object.y_velocity=object.y_velocity-dampening_constant*math.sin(velocity_angle)
        object.x_velocity=object.x_velocity-dampening_constant*math.cos(velocity_angle)
    elif object.x_velocity<=0 and object.y_velocity>=0:
        velocity_angle=0.0
        if object.y_velocity==0:
            velocity_angle=0.0
        elif object.x_velocity==0:
            velocity_angle=90.0
        else:
            velocity_angle=math.atan(object.y_velocity/object.x_velocity)
        object.y_velocity=object.y_velocity+dampening_constant*math.sin(velocity_angle)
        object.x_velocity=object.x_velocity+dampening_constant*math.cos(velocity_angle)
        


    if object.x_velocity<0.05 and object.x_velocity>-0.05:
        object.x_velocity=0
    if object.y_velocity<0.05 and object.y_velocity>-0.05:
            object.y_velocity=0

def detect_key(key):
    key_detect=pygame.key.get_pressed()
    if key_detect[key]:
        return True