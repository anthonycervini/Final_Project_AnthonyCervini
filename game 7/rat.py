#creating a sprite class for the enemy, rat

import pygame
import random
from parameters import *
MAX_SPEED = 3.5
MIN_SPEED = 1.0

class Rat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/rat.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(min_speed, max_speed)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
    def draw(self, filth):
        filth.blit(self.image, self.rect)

rats = pygame.sprite.Group()
