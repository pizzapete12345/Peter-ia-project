import pygame
import math

pygame.init()
from characters import Star, player
from vector_functions import detect_key

starlist = []
with open("starlist.txt", "r") as file:

    for line in file:

        word = ""
        name = ""
        type = ""
        increaser = 0
        coordinates = ""

        for i in line:
            if i == "/":
                if increaser == 0:
                    name = word
                    increaser = 1
                elif increaser == 1:
                    type = word
                    increaser = 2
                elif increaser == 2:
                    coordinates = tuple(float(x) for x in word.split(","))
                    increaser = 0
                word = ""
            else:
                word = word + i

        starlist.append(Star(name, coordinates, type))

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
current_screen = 0

font = pygame.font.Font(None, 50)
text_vdisplay = font.render(
    f"velocity = {str(round(math.sqrt(player.x_velocity**2+player.y_velocity**2),2))}",
    True,
    (255, 255, 255),
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if current_screen == 0:
        if detect_key(pygame.K_SPACE):
            current_screen = 1
        screen.blit(
            font.render("W,D to move forwards and backwards", True, (255, 255, 255)),
            (500, 330),
        )
        screen.blit(font.render("A,D to rotate", True, (255, 255, 255)), (500, 290))
        screen.blit(font.render("B to brake", True, (255, 255, 255)), (500, 250))
        screen.blit(font.render("R to reset", True, (255, 255, 255)), (500, 210))
        screen.blit(
            font.render(
                "Use the number keys to enable/disable views", True, (255, 255, 255)
            ),
            (500, 170),
        )
        screen.blit(
            font.render("press space to start", True, (255, 255, 255)), (500, 130)
        )

    if current_screen == 1:
        player.render(screen)
        player.movement()

        for i in starlist:
            i.render(screen)
            i.update(player)

        screen.blit(text_vdisplay, (0, 0))
        text_vdisplay = font.render(
            f"velocity = {str(round(math.sqrt(player.x_velocity**2+player.y_velocity**2),2))}",
            True,
            (255, 255, 255),
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
