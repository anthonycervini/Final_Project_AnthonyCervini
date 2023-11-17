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

#Main loop
running = True
background = screen.copy()
draw_background(background)

#draw rats
for _ in range(8):
    rats.add(Rat(random.randint(screen_width, screen_width*1.5),random.randint(tile_size, screen_height)))

#add in the gunner
gunner = Gunner(screen_width/2, screen_height/2)

#initialize the score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 45)
#text = score_font.render(f"{score}", True, (255, 0,0))

#load the sound fx
rat_squeak = pygame.mixer.Sound("../assets/sounds/rat_squeak.mp3")

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
    screen.blit(background, (0, 0))
    #draw enemies
    rats.update()
    #draw gunner
    gunner.update()

    #check for gunner and rat collisions
    result = pygame.sprite.spritecollide(gunner, rats, True)
    if result:
        pygame.mixer.Sound.play(rat_squeak)
        score += len(result)
        for _ in range(len(result)):

             rats.add(Rat(random.randint(screen_width, screen_width + 20), random.randint(tile_size, screen_height - 2 *tile_size)))

    # check if rats have left the screen
    for rat in rats:
        if rat.rect.x < - rat.rect.width:
            rats.remove(rat)
            rats.add(Rat(random.randint(screen_width, screen_width + 50),
                         random.randint(tile_size, screen_height - 2 * tile_size)))


    #draw the sprites
    rats.draw(screen)
    gunner.draw(screen)

    #draw score
    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (screen_width - tile_size, 0))

    #update what is displayed
    pygame.display.flip()

    #establish frame rate
    clock.tick(120)

#quit the game
pygame.quit()
sys.exit()