import pygame
import math
import sys

#Základní nastavení - začátek
WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet Simulation")
pygame.init()
#Základní nastavení- konec

intro_image = pygame.image.load("pictures/PS_intro.png")
intro_duration = 5000
intro_start_time = pygame.time.get_ticks()


#barvy, fonty - začátek
WHITE = (255,255,255)
YELLOW =(255,255,0)
BLUE = (100 ,149, 237)
RED = (188,39,50)
DARK_GREY = (80,78,81)
BLACK = (0,0,0)
GREEN = (80, 200, 120)
TEXT_COL = (255, 0, 255)
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
#barvy, fonty - konec


#obrázky - začátek
start_img = pygame.image.load("pictures/start.png").convert_alpha()
exit_img = pygame.image.load("pictures/menu.png").convert_alpha()
button_image_tr1 = pygame.transform.scale(start_img, (220, 145))
button_image_tr2 = pygame.transform.scale(exit_img, (1200, 800))
#obrázky - konec

#velikost tlačítka - začátek
button_width = 190
button_widt2 = 400
button_height = 115
button_height2 = 600
button_x = (button_height) // 1
button_y = (button_height2) // 1
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

start_button_rect = start_img.get_rect()
start_button_rect2 = exit_img.get_rect()
#velikost tlačítka - konec


#když tak pro napsání textu / nepoužito
def draw_text(text, font, text_col, x, y,):
  img = font.render(text, True, text_col)
  WIN.blit(img, (x, y))


#hlavní třída
class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 200 / AU #jeden AU se rovná 200 pixelů
    TIMESTEP = 3600*24 #1 den
    
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x 
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0


        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point 
                x = x * self.SCALE  + WIDTH /2
                y = y * self.SCALE + HEIGHT /2 
                updated_points.append((x, y))
            
            pygame.draw.lines(win, self.color, False, updated_points, 2)


        pygame.draw.circle(win, self.color, (x, y), self.radius )

    def attraction(self, other):

        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2+ distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance 

        force = self.G * self.mass * other.mass / distance **2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force 
        force_y = math.sin(theta) * force

        #ukádání do souboru
        with open("data.txt", "a") as f:
            data = distance, force, theta 
            f.write( "\n")
            f.write("Délka, síla, úhel\n")
            f.write(str(data))
            f.write("\n")


        return force_x, force_y



    def update_position(self, planets):

        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue 
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        #made by cyberft-pdf

game_start = False


def main():
    run  = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,30, YELLOW, 1.989 * 10**30 )
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24) 
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000


    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = 35.02 * 1000
    #zde můžu přidat další planety

    planets = [sun,earth,mars, mercury, venus]



    
    while run:
        clock.tick(60)


        WIN.fill((0,0,0))
        #pygame.display.update()

        draw_text("", font, WHITE,160,300)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 


        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update() 
    
    pygame.quit()


#hlavní while loop
show_intro = True
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    current_time = pygame.time.get_ticks()
    #začatek PL_foto
    if show_intro:
            WIN.blit(intro_image, (0, 0))
            pygame.display.flip()

            if current_time - intro_start_time >= intro_duration:
                show_intro = False
    #Pokračování na simulaci
    else:
        WIN.blit(button_image_tr2, (0, 0))  
        WIN.blit(button_image_tr1, button_rect,)
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
                main()



    pygame.display.flip()  

pygame.quit()
