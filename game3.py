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

#building the screen dimensions, choosing an image, setting a caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('trash background')
image = pygame.image.load("assets/sprites/trash_background.jpg")

#adding game title and font
custom_font = pygame.font.Font("assets/fonts/CrimesTimesSix.ttf", 100)

#creating the filth function to blit the screen
def draw_background(filth):
    trash = pygame.transform.scale(image,(image.get_width()*3, image.get_height()*4)) #scaling custom image dimensions to fit my screen

    for x in range(0, screen_width, screen_width):
        for y in range(0,screen_height, screen_height):
            filth.blit(trash, (x,y))

    #drawing the game title text
    text = custom_font.render("Garbage Gladiator", True, (255,0,0))
    filth.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))

 # Main loop
running = True
background = screen.copy()
draw_background(background)

#draw the enemy rats using new class
for _ in range(8):
    rats.add(Rat(random.randint(tile_size, screen_width-tile_size), random.randint(tile_size, screen_height-tile_size)))

while running:
    screen.blit(background, (0,0))
    rats.draw(background)
    pygame.display.flip()

#adding ability to quit pygame
pygame.quit()
