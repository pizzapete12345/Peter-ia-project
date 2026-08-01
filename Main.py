import pygame
from characters import Player,Star

player = Player()
star = Star((33,22))

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
    star.render(screen)
    star.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


