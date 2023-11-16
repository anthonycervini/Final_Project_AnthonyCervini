import pygame
import random
import sys

from parameters import *
from rat import Rat, rats
from background import draw_background
from gunner import Gunner

#initialize pygame
pygame.init()

#loading the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('raccoon unleashed')

#establishing frame rate
clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

#draw enemies
for _ in range(8):
    rats.add(Rat(random.randint(screen_width, screen_width*1.5),random.randint(tile_size, screen_height)))

#add in the gunner
gunner = Gunner(screen_width/2, screen_height/2)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #control the gunner movement with keyboard
        gunner.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gunner.move_up()
            if event.key == pygame.K_DOWN:
                gunner.move_down()
            if event.key == pygame.K_LEFT:
                gunner.move_left()
            if event.key == pygame.K_RIGHT:
                gunner.move_right()
    #draw the background
    screen.blit(background, (0,0))
    #draw enemies
    rats.update()
    #draw gunner
    gunner.update()

    rats.draw(screen)
    gunner.draw(screen)

    # check if rats have left the screen
    for rat in rats:
        if rat.rect.x < - rat.rect.width:
            rats.remove(rat)
            rats.add(Rat(random.randint(screen_width, screen_width + 50),
                         random.randint(tile_size, screen_height - 2 * tile_size)))
    #update what is displayed
    pygame.display.flip()

    #establish frame rate
    clock.tick(120)

#quit the game
pygame.quit()
sys.exit()