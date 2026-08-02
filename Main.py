import pygame
import math
pygame.init()
from characters import Player,Star

player = Player()
star_1 = Star((100,100),0,0,(255,255,255))
star_2 = Star((500,500),0,0,(255,255,255))
star_3 = Star((200,400),0,0,(255,255,255))

font=pygame.font.Font(None, 50)
text_vdisplay=font.render(str(math.sqrt(player.x_velocity**2+player.y_velocity**2)),True,(255,255,255))


pygame.init()
screen = pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill((0,0,0))

    player.render(screen)
    player.movement()
    star_1.render(screen)
    star_1.update(player)
    star_2.render(screen)
    star_2.update(player)
    star_3.render(screen)
    star_3.update(player)

    screen.blit(text_vdisplay,(0,0))
    text_vdisplay=font.render(f"velocity = {str(math.sqrt(player.x_velocity**2+player.y_velocity**2))}",True,(255,255,255))
    text_ydisplay=font.render(f"y_velocity = {str(player.y_velocity)}",True,(255,255,255))
    screen.blit(text_ydisplay,(0,50))
    text_xdisplay=font.render(f"x_velocity = {str(player.x_velocity)}",True,(255,255,255))
    screen.blit(text_xdisplay,(0,100))



    pygame.display.flip()
    clock.tick(60)


pygame.quit()


