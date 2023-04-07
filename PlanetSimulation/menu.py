import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen (width, height).
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Button Example")

# Define the button rectangle
button_rect = pygame.Rect(200, 200, 100, 50)

# Set the default button color
button_color = GREEN

# Function to be called when the button is clicked
def button_clicked():
    print("Button clicked!")

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
                # Call the function when the button is clicked
                button_clicked()

    # --- Draw ---
    # Clear the screen
    screen.fill(WHITE)

    # Draw the button rectangle
    pygame.draw.rect(screen, button_color, button_rect)

    # Update the screen
    pygame.display.flip()

# Quit the program
pygame.quit()