#creating a sprite class for the food

import pygame
import random
from parameters import *

MAX_SPEED = 3.5
MIN_SPEED = 1.0

class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/food.jpg").convert()
        self.image.set_colorkey((252,252,252))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(min_speed, max_speed)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        self.rect.x = self.x
    def draw(self, filth):
        filth.blit(self.image, self.rect)

foods = pygame.sprite.Group()
