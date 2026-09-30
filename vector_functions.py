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

def rgb_to_xyz(color):
    corrected_rgb=(color[0]/255,color[1]/255,color[2]/255)

    if color[0]<=255:
        linearr=color[0]/12.92
    else:
        linearr=((color[0]+0.055)/1.055)**2.4

    if color[1]<=255:
        linearg=color[1]/12.92
    else:
        linearg=((color[1]+0.055)/1.055)**2

    if color[2]<=255:
        linearb=color[2]/12.92
    else:
        linearb=((color[2]+0.055)/1.055)**2

    return (linearr*0.4125+linearg*0.3576+linearb*0.1804,linearr*0.2127+linearg*0.7152+linearb*0.0722,linearr*0.0193+linearg*0.1192+linearb*0.9503)


def actual_redshift(frame,object):
    xyz=rgb_to_xyz(object.color)
    factor=redshift(frame,object)

    shifted=(xyz[0]*factor,xyz[1]*factor,xyz[2]*factor)

    linear=(3.2404542 * shifted[0] - 1.5371385 * shifted[1] - 0.4985314 * shifted[2],-0.9692660 * shifted[0] + 1.8760108 * shifted[1] + 0.0415560 * shifted[2],0.0556434 * shifted[0] - 0.2040259 * shifted[1] + 1.0572252 * shifted[2])

    if linear[0]<=0.0031318:
        r=linear[0]*12.92
    else:
        r=1.055*(linear[0])**(1/2.4)-0.055
    if linear[1]<=0.0031318:
        g=linear[1]*12.92
    else:
        g=1.055*(linear[1])**(1/2.4)-0.055
    if linear[2]<=0.0031318:
        b=linear[2]*12.92
    else:
        b=1.055*(linear[2])**(1/2.4)-0.055

    return (r*70,g*70,b*70)
