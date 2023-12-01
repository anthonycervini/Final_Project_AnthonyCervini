import pygame
from pygame import mixer
import sys

from parameters import *
from food import foods
from rat import rats
from cottoncandy import cottons
from background import draw_background, add_rats, add_food, add_cottoncandy
from gunner import Gunner
from second_player import Ractwo

#initialize pygame
pygame.init()

#loading the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('raccoons unleashed')

#adding background music to play continuously
mixer.init()
mixer.music.load("../assets/sounds/electronic.ogg")
mixer.music.play()

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

#draw cotton candy
add_cottoncandy(1)

#add in the players
gunner = Gunner(screen_width/2, screen_height/2)
second_player = Ractwo(screen_width/3, screen_height/3)

#initialize the score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 45)

#load the sound fx
rat_squeak = pygame.mixer.Sound("../assets/sounds/rat_squeak.mp3")
crunch = pygame.mixer.Sound("../assets/sounds/crunch.mp3")
ohno = pygame.mixer.Sound("../assets/sounds/ohno.wav")
extra_life = pygame.mixer.Sound("../assets/sounds/extra_life.mp3")

#add life photos and lives
life_icon = pygame.image.load("../assets/sprites/raccoon_lives.png")
life_icon.set_colorkey((255, 255, 255))
lives = num_lives

#adding a pause screen
def paused():
    pause = True
    while pause:
        screen.fill((255, 255, 255))
        condition = score_font.render("Paused: Press any key to continue", True, (64, 224, 228))
        screen.blit(condition, (screen_width / 2 - condition.get_width()/2, screen_height / 2))
        pygame.display.flip()
        mixer.music.pause()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                pause = False
                mixer.music.unpause()

#while loop enabling game to run, player movement with keys
while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control the gunner movement with keyboard
        gunner.stop()
        #second_player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gunner.move_up()
            if event.key == pygame.K_DOWN:
                gunner.move_down()
            if event.key == pygame.K_LEFT:
                gunner.move_left()
            if event.key == pygame.K_RIGHT:
                gunner.move_right()
            if event.key == pygame.K_p:
                pause = True
                paused()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                second_player.move_up()
            if event.key == pygame.K_s:
                second_player.move_down()
            if event.key == pygame.K_a:
                second_player.move_left()
            if event.key == pygame.K_d:
                second_player.move_right()
        if event.type == pygame.KEYUP:
            second_player.stop()

    #update the background
    screen.blit(background, (0, 0))
    #draw enemies
    rats.update()
    #draw food
    foods.update()
    #draw cotton candy
    cottons.update()
    #draw players
    gunner.update()
    second_player.update()


    #check for gunner and rat collisions
    occurrence = pygame.sprite.spritecollide(gunner, rats, True)
    if occurrence:
        pygame.mixer.Sound.play(rat_squeak)
        lives -= len(occurrence)
        add_rats(len(occurrence))

    #check for gunner and food collisions
    instance = pygame.sprite.spritecollide(gunner, foods, True)
    if instance:
        pygame.mixer.Sound.play(crunch)
        score += len(instance)
        add_food(len(instance))

    #check for gunner and cotton candy collisions
    result = pygame.sprite.spritecollide(gunner, cottons, True)
    if result:
        pygame.mixer.Sound.play(extra_life)
        score += len(result)
        add_cottoncandy(len(result))
        lives += len(result)

    # check for second player and rat collisions
    occurrence = pygame.sprite.spritecollide(second_player, rats, True)
    if occurrence:
        pygame.mixer.Sound.play(rat_squeak)
        lives -= len(occurrence)
        add_rats(len(occurrence))

    # check for second player and food collisions
    instance = pygame.sprite.spritecollide(second_player, foods, True)
    if instance:
        pygame.mixer.Sound.play(crunch)
        score += len(instance)
        add_food(len(instance))

    # check for second player and cotton candy collisions
    result = pygame.sprite.spritecollide(second_player, cottons, True)
    if result:
        pygame.mixer.Sound.play(extra_life)
        score += len(result)
        add_cottoncandy(len(result))
        lives += len(result)

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

    #check if cotton candy left the screen:
    for cottoncandy in cottons:
        if cottoncandy.rect.y > screen_height:
            cottons.remove(cottoncandy)
            add_cottoncandy(1)



    #draw the sprites
    rats.draw(screen)
    foods.draw(screen)
    cottons.draw(screen)
    gunner.draw(screen)
    second_player.draw(screen)

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
message = score_font.render("THE RATS WON", True, (255, 0, 0))
screen.blit(message, (screen_width/2 - message.get_width()/2, screen_height/2))

score_text = score_font.render(f"Score: {score}", True, (255, 0, 0))
screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 + score_text.get_height()))

pygame.display.flip()

mixer.music.stop()

pygame.mixer.Sound.play(ohno)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
