import pygame
from parameters import *

#making a sprite class for the player

class Ractwo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("../assets/sprites/other_raccoon.jpg").convert()
        self.forward_image.set_colorkey((255, 255, 255))
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1 * player_speed

    def move_down(self):
        self.y_speed = player_speed

    def move_left(self):
        self.x_speed = -1 * player_speed
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = player_speed
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > screen_width - tile_size:
            self.x = screen_width - tile_size
        if self.x < 0:
            self.x = 0
        if self.y > screen_height - tile_size:
            self.y = screen_height - tile_size
        if self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, filth):
        filth.blit(self.image, self.rect)

