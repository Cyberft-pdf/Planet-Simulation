import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Pygame Window")

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update game state
    # ...

    # draw screen
    screen.fill((255, 255, 255))  # fill with white color
    # ...

    pygame.display.flip()  # update screen

pygame.quit()