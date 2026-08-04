import pygame
import math
pygame.init()
from characters import Player,Star
from vector_functions import detect_key

player = Player()
star_1 = Star((100,100),0,0,(255,255,255))
star_2 = Star((500,500),0,0,(255,255,255))
star_3 = Star((200,400),0,0,(255,255,255))



pygame.init()
screen = pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
running = True
current_screen=0


font=pygame.font.Font(None, 50)
text_vdisplay=font.render(f"velocity = {str(round(math.sqrt(player.x_velocity**2+player.y_velocity**2),2))}",True,(255,255,255))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill((0,0,0))

    if current_screen == 0:
        if detect_key(pygame.K_SPACE):
            current_screen=1
        screen.blit(font.render("W,A,S,D for movement",True,(255,255,255)),(640,330))
        screen.blit(font.render("Q,E to rotate",True,(255,255,255)),(640,290))
        screen.blit(font.render("B to brake",True,(255,255,255)),(640,250))
        screen.blit(font.render("R to reset",True,(255,255,255)),(640,210))
        screen.blit(font.render("press space to start",True,(255,255,255)),(640,170))



    if current_screen == 1:
        player.render(screen)
        player.movement()
        star_1.render(screen)
        star_1.update(player)
        star_2.render(screen)
        star_2.update(player)
        star_3.render(screen)
        star_3.update(player)

        screen.blit(text_vdisplay,(0,0))
        text_vdisplay=font.render(f"velocity = {str(round(math.sqrt(player.x_velocity**2+player.y_velocity**2),2))}",True,(255,255,255))
        text_ydisplay=font.render(f"y_velocity = {str(round(player.y_velocity,2))}",True,(255,255,255))
        screen.blit(text_ydisplay,(0,50))
        text_xdisplay=font.render(f"x_velocity = {str(round(player.x_velocity,2))}",True,(255,255,255))
        screen.blit(text_xdisplay,(0,100))



    pygame.display.flip()
    clock.tick(60)


pygame.quit()


