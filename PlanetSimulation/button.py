import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen (width, height).
screen_size = (1600, 1000)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Button Example")

# Load the button image
button_img = pygame.image.load("start.png")

# Define the button rectangle
button_rect = pygame.Rect(200, 690, 300, 600)

# Set the default button color
button_color = GREEN
button_img = pygame.transform.scale(button_img, (button_img.get_width()//5, button_img.get_height()//5))
# Main loop
running = True
while running:

    # --- Event Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check if the left mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is on the button
            if button_rect.collidepoint(event.pos):
                # Change the button color
                button_color = RED

    # --- Draw ---
    # Clear the screen
    screen.fill(WHITE)

    # Draw the button rectangle
    pygame.draw.rect(screen, button_color)

    # Draw the button image
    screen.blit(button_img, button_rect)

    # Update the screen
    pygame.display.flip()

# Quit the program
pygame.quit()