import pygame
import random
import time
from pygame.locals import *
#initializing pygame window
pygame.init()
pygame.display.set_caption("Recycling Game")
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#bin class
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image, (35,50))
        self.rect = self.image.get_rect()

#non-recycle class
class nr (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("toxic.png")
        self.image = pygame.transform.scale(self.image, (30,40))
        self.rect = self.image.get_rect()

#recycle class
class r (pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (30,40))
        self.rect = self.image.get_rect()

recycle = ["carton-box.png", "paperbag.png", "straw.png"]
#creating groups

ritems = pygame.sprite.Group()
nritems = pygame.sprite.Group()
allitems = pygame.sprite.Group()

for i in range(40):
    picker = r(random.choice(recycle))
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
