import math
import pygame

def rotates(list, amount):
    changed = []
    for point in list:
        vector = pygame.math.Vector2(point)
        changed.append(vector.rotate(amount))
    return changed


def dampening(object, dampening_constant):
    if object.x_velocity >= 0 and object.y_velocity >= 0:
        velocity_angle = 0.0
        if object.y_velocity == 0:
            velocity_angle = 0.0
        elif object.x_velocity == 0:
            velocity_angle = 90.0
        else:
            velocity_angle = math.atan(object.y_velocity / object.x_velocity)
        object.y_velocity = object.y_velocity - dampening_constant * math.sin(
            velocity_angle
        )
        object.x_velocity = object.x_velocity - dampening_constant * math.cos(
            velocity_angle
        )
    elif object.x_velocity <= 0 and object.y_velocity <= 0:
        velocity_angle = 0.0
        if object.y_velocity == 0:
            velocity_angle = 0.0
        elif object.x_velocity == 0:
            velocity_angle = 90.0
        else:
            velocity_angle = math.atan(object.y_velocity / object.x_velocity)
        object.y_velocity = object.y_velocity + dampening_constant * math.sin(
            velocity_angle
        )
        object.x_velocity = object.x_velocity + dampening_constant * math.cos(
            velocity_angle
        )
    elif object.x_velocity >= 0 and object.y_velocity <= 0:
        velocity_angle = 0.0
        if object.y_velocity == 0:
            velocity_angle = 0.0
        elif object.x_velocity == 0:
            velocity_angle = 90.0
        else:
            velocity_angle = math.atan(object.y_velocity / object.x_velocity)
        object.y_velocity = object.y_velocity - dampening_constant * math.sin(
            velocity_angle
        )
        object.x_velocity = object.x_velocity - dampening_constant * math.cos(
            velocity_angle
        )
    elif object.x_velocity <= 0 and object.y_velocity >= 0:
        velocity_angle = 0.0
        if object.y_velocity == 0:
            velocity_angle = 0.0
        elif object.x_velocity == 0:
            velocity_angle = 90.0
        else:
            velocity_angle = math.atan(object.y_velocity / object.x_velocity)
        object.y_velocity = object.y_velocity + dampening_constant * math.sin(
            velocity_angle
        )
        object.x_velocity = object.x_velocity + dampening_constant * math.cos(
            velocity_angle
        )

    if object.x_velocity < 0.02 and object.x_velocity > -0.02:
        object.x_velocity = 0
    if object.y_velocity < 0.02 and object.y_velocity > -0.02:
        object.y_velocity = 0


def detect_key(key):
    key_detect = pygame.key.get_pressed()
    if key_detect[key]:
        return True


def lorentz_transformation(frame, object_positition, coordinates):
    output = []

    relative_xvelocity = frame.x_velocity
    relative_yvelocity = frame.y_velocity

    relative_velocity = math.sqrt(relative_xvelocity**2 + relative_yvelocity**2)
    if relative_velocity < 10e-12:
        return coordinates

    lorentz_factor = 1 / math.sqrt(1 - (relative_velocity**2))

    for i in coordinates:

        x = i[0] + object_positition[0] - 640
        y = i[1] + object_positition[1] - 360
        dotproduct = x * relative_xvelocity + y * relative_yvelocity
        the_part_that_changes = dotproduct / relative_velocity**2

        parralelx = the_part_that_changes * relative_xvelocity
        parralely = the_part_that_changes * relative_yvelocity
        perpendiculerx = x - parralelx
        perpendiculery = y - parralely

        x = perpendiculerx + parralelx / lorentz_factor
        y = perpendiculery + parralely / lorentz_factor
        output.append((x + 640 - object_positition[0], y + 360 - object_positition[1]))

    return output

def translate(coordinate_list,position):
    output=[]
    for i in coordinate_list:
        output.append((i[0]+position[0],i[1]+position[1]))
    return(output)

def redshift(frame,object):

    magnitude=math.sqrt((object.position[0]-640)**2+(object.position[1]-360)**2)

    if magnitude<10e-12:
        return 1

    antifloat_check_variable=math.sqrt(frame.x_velocity**2+frame.y_velocity**2)

    if antifloat_check_variable<10e-12:
        return 1

    relative_velocity=(frame.x_velocity*(object.position[0]-640)+frame.y_velocity*(object.position[1]-360))/magnitude


    velocity_anlge=math.acos(frame.x_velocity/magnitude)
    position_angle=math.atan((object.position[1]-360)/(object.position[0]-640))
    relative_angle=position_angle-velocity_anlge


    return math.sqrt(1-(relative_velocity**2))/(1-(relative_velocity*math.cos(relative_angle)))



def actual_redshift(frame,object):

    factor=redshift(frame,object)

    if factor>1:
        factor=1




    
    color=object.color

    red=color[0]*factor  
    blue=color[1]*factor**2      
    green=color[2]*factor**3  

    if red<10e-12:
        red=0
    elif red>255:
        red=255
    if blue<10e-12:
        blue=0
    elif blue>255:
        blue=255
    if green<10e-12:
        green=0
    elif green>255:
        green=255

    output=(red,blue,green)

    return output




