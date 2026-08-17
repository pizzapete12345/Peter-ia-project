import math
import pygame


def rotates(point,amount):
    vector=pygame.math.Vector2(point)
    return(vector.rotate(amount))


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

def lorentz_calculator(frame):
    relative_xvelocity=frame.x_velocity
    relative_yvelocity=frame.y_velocity
    relative_velocity=math.sqrt(relative_xvelocity**2+relative_yvelocity**2)
    return 1/math.sqrt(1-(relative_velocity**2))

def lorentz_transformation(frame,object_positition,coordinates):
    output=[]



    relative_xvelocity=frame.x_velocity
    relative_yvelocity=frame.y_velocity

    relative_velocity=math.sqrt(relative_xvelocity**2+relative_yvelocity**2)
    if relative_velocity<10E-12:
        return(coordinates)

    lorentz_factor=1/math.sqrt(1-(relative_velocity**2))

    for i in coordinates:
        
        x=i[0]+object_positition[0]-640
        y=i[1]+object_positition[1]-360
        dotproduct=x*relative_xvelocity+y*relative_yvelocity
        the_part_that_changes=dotproduct/relative_velocity**2

        parralelx=the_part_that_changes*relative_xvelocity
        parralely=the_part_that_changes*relative_yvelocity
        perpendiculerx=x-parralelx
        perpendiculery=y-parralely

        x=perpendiculerx+parralelx/lorentz_factor
        y=perpendiculery+parralely/lorentz_factor
        output.append((x+640-object_positition[0],y+360-object_positition[1]))

    return(output)
 

def penrose_transformation(frame,object_position,vertex):

    relative_xvelocity=frame.x_velocity
    relative_yvelocity=frame.y_velocity

    relative_velocity=math.sqrt(relative_xvelocity**2+relative_yvelocity**2)
    x=vertex[0]+object_position[0]-640
    y=vertex[1]+object_position[1]-360
    if relative_velocity<10E-12:
        return (x,y)

    lorentz_factor=1/math.sqrt(1-(relative_velocity**2))

    dotproduct=x*relative_xvelocity+y*relative_yvelocity
    the_part_that_changes=dotproduct/relative_velocity**2

    parralelx=the_part_that_changes*relative_xvelocity
    parralely=the_part_that_changes*relative_yvelocity
    perpendiculerx=x-parralelx
    perpendiculery=y-parralely

    x=perpendiculerx+parralelx/lorentz_factor
    y=perpendiculery+parralely/lorentz_factor
    vertex=(x,y)

    return(vertex)
 


