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
        


    if object.x_velocity<0.2 and object.x_velocity>-0.2:
        object.x_velocity=0
    if object.y_velocity<0.2 and object.y_velocity>-0.2:
            object.y_velocity=0

def detect_key(key):
    key_detect=pygame.key.get_pressed()
    if key_detect[key]:
        return True

def lorentz_transformation(frame,object,coordinates):
    print("hello")
    output=[]
    speed_of_light=10


    relative_xvelocity=frame.x_velocity
    relative_yvelocity=frame.y_velocity
    relative_velocity=math.sqrt(relative_xvelocity**2+relative_yvelocity**2)
    print(relative_velocity)
    if relative_velocity<10E-12:
        return(coordinates)
    unit_vector=(relative_xvelocity/relative_velocity,relative_yvelocity/relative_velocity)


    
    lorentz_factor=1/math.sqrt(1-(relative_velocity**2))
    print(lorentz_factor)


    for i in coordinates:
        
        x=i[0]+object.position[0]-641
        y=i[1]+object.position[1]-361
        distance=math.sqrt(x**2+y**2)
        x=lorentz_factor*(x-relative_xvelocity*unit_vector[0])
        y=lorentz_factor*(y-relative_yvelocity*unit_vector[1])
        output.append((x+641-object.position[0],y+361-object.position[1]))

    return(output)





