import pygame
import random
from parameters import *

image = pygame.image.load("../assets/sprites/trash_background.jpg")


#loading the established background
def draw_background(filth):
    trash = pygame.transform.scale(image,(image.get_width()*3, image.get_height()*4)) #scaling custom image dimensions to fit my screen
    #filling the screen with transformed image
    for x in range(0, screen_width, screen_width):
        for y in range(0,screen_height, screen_height):
            filth.blit(trash, (x,y))

    #adding game title and font
    custom_font = pygame.font.Font("../assets/fonts/CrimesTimesSix.ttf", 100)

    #drawing the game caption text
    text = custom_font.render("Garbage Gladiator", True, (255,0,0))

    #printing text in the middle
    filth.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))

