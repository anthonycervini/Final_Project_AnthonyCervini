import pygame
import random
from parameters import *
from rat import Rat, rats
from food import Food, foods
from cottoncandy import Cotton, cottons

#loading the established background
def draw_background(filth):
    image = pygame.image.load("../assets/sprites/trash_background.jpg")
    image = pygame.transform.scale(image, (image.get_width()*3, image.get_height()*4)) #scaling custom image dimensions to fit my screen
    #filling the screen with transformed image
    #for x in range(0, screen_width, tile_size):
    #    for y in range(0,screen_height, tile_size):
            #filth.blit(image, (x, y))
    filth.blit(image, (0, 0))

    #adding game title and font
    custom_font = pygame.font.Font("../assets/fonts/CrimesTimesSix.ttf", 100)

    #drawing the game caption text
    text = custom_font.render("Garbage Gladiator", True, (255,0,0))

    #printing text in the middle
    filth.blit(text, (screen_width / 2 - text.get_width() / 2, 0))

def add_rats(num_rats):
    for _ in range(num_rats):
        rats.add(Rat(random.randint(screen_width, screen_width + 50),
                     random.randint(0, screen_height)))

def add_food(num_foods):
    for _ in range(num_foods):
        foods.add(Food(random.randint(10, 790),
                     random.randint(0, 0)))

def add_cottoncandy(num_cottons):
    for _ in range(num_cottons):
        cottons.add(Cotton(random.randint(10, 790),
                       random.randint(0, 0)))

# def add_lives(num_lives):
#     for _ in range(num_lives):
#         num_lives += 1