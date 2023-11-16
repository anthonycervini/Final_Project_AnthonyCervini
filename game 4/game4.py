import pygame
import random
import sys
from rat import Rat, rats #imports the class and sprite group

#initializing pygame
pygame.init()

#defining screen parameters
screen_width = 800
screen_height = 600
tile_size = 64

#building the screen dimensions, choosing an image
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('trash background')
image = pygame.image.load("../assets/sprites/trash_background.jpg")

#adding game title and font
custom_font = pygame.font.Font("../assets/fonts/CrimesTimesSix.ttf", 100)

#drawing the game caption text
text = custom_font.render("Garbage Gladiator", True, (255,0,0))

#adding clock object
clock = pygame.time.Clock()
#creating the filth function to blit the screen
def draw_background(filth):
    trash = pygame.transform.scale(image,(image.get_width()*3, image.get_height()*4)) #scaling custom image dimensions to fit my screen

    for x in range(0, screen_width, screen_width):
        for y in range(0,screen_height, screen_height):
            filth.blit(trash, (x,y))
    filth.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))

 # Main loop
running = True
background = screen.copy()
draw_background(background)

#draw the enemy rats using new class
for _ in range(8):
    rats.add(Rat(random.randint(tile_size, screen_width-tile_size), random.randint(tile_size, screen_height-tile_size)))

while running:
    #drawing the background
    screen.blit(background, (0,0))

    #updating enemy location
    rats.update()

    #check if rats have left the screen
    for rat in rats:
        if rat.rect.x < - rat.rect.width:
            rats.remove(rat)
            rats.add(Rat(random.randint(screen_width, screen_width + 50), random.randint(tile_size, screen_height - 2 * tile_size)))
    #drawing the rats on the screen
    rats.draw(screen)
    #updating the display
    pygame.display.flip()
    #determine frame rate
    clock.tick(60)

#adding ability to quit pygame
pygame.quit()
sys.exit()