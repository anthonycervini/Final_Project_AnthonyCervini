import pygame
import random
import sys

#initializing pygame
pygame.init()

#defining parameters
screen_width = 800
screen_height = 600
tile_size = 64

#building the screen dimensions, choosing an image, setting a caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('trash background')
image = pygame.image.load("assets/sprites/trash_background.jpg")

#creating the filth function to blit the screen
def draw_background(filth):
    trash = pygame.transform.scale(image,(image.get_width()*3, image.get_height()*4)) #scaling custom image dimensions to fit my screen

    for x in range(0, screen_width, screen_width):
        for y in range(0,screen_height, screen_height):
            filth.blit(trash, (x,y))

#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    screen.blit(background, (0,0))
    pygame.display.flip()

#adding ability to quit pygame
pygame.quit()
