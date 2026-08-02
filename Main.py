import pygame
from characters import Player,Star

player = Player()
star_1 = Star((100,100),0,0)
star_2 = Star((500,500),0,0)
star_3 = Star((200,400),0,0)


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
    pygame.display.flip()
    clock.tick(60)


pygame.quit()


