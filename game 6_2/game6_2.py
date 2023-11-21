import pygame
import random
import sys

from parameters import *
from food import foods
from rat import rats
from background import draw_background, add_rats, add_food
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

#draw the enemy rats
add_rats(5)

#draw foods
add_food(3)

#add in the gunner
gunner = Gunner(screen_width/2, screen_height/2)

#initialize the score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 45)

#load the sound fx
rat_squeak = pygame.mixer.Sound("../assets/sounds/rat_squeak.mp3")
crunch = pygame.mixer.Sound("../assets/sounds/crunch.mp3")
ohno = pygame.mixer.Sound("../assets/sounds/ohno.wav")

#add life photos and lives
life_icon = pygame.image.load("../assets/sprites/raccoon_lives.png")
life_icon.set_colorkey((255,255,255))
lives = num_lives

while lives > 0 and running:
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
    #draw food
    foods.update()
    #draw gunner
    gunner.update()

    #check for gunner and rat collisions
    result = pygame.sprite.spritecollide(gunner, rats, True)
    if result:
        pygame.mixer.Sound.play(rat_squeak)
        lives -= len(result)
        add_rats(len(result))

    #check for gunner and food collisions
    result = pygame.sprite.spritecollide(gunner, foods, True)
    if result:
        pygame.mixer.Sound.play(crunch)
        score += len(result)
        add_food(len(result))

    # check if rats have left the screen
    for rat in rats:
        if rat.rect.x < - rat.rect.width:
            rats.remove(rat)
            add_rats(1)



    # check if food has left the screen
    for food in foods:
        if food.rect.y > screen_height:
            foods.remove(food)
            add_food(1)


    #draw the sprites
    rats.draw(screen)
    foods.draw(screen)
    gunner.draw(screen)

    #draw score
    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (screen_width - tile_size, screen_height - tile_size))

    #draw lives
    for i in range(lives):
        screen.blit(life_icon, (i*tile_size, screen_height - tile_size))

    #update what is displayed
    pygame.display.flip()

    #establish frame rate
    clock.tick(120)

#game over screen
message = score_font.render("THE RATS WON", True, (0,0,0))
screen.blit(message, (screen_width/2 - message.get_width()/2, screen_height/2))

score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (screen_width/2 - score_text.get_width()/2 , screen_height/2 + score_text.get_height()))

pygame.display.flip()

pygame.mixer.Sound.play(ohno)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

