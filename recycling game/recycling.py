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
score = 0
text = pygame.font.SysFont("arial",30)
seconds = 20
start_time = time.time()
scoretext = text.render("SCORE:"+str(score),True,"black")

def bg(img):
    backg = pygame.image.load(img)
    backgscale = pygame.transform.scale(backg, (1000,600))
    screen.blit(backgscale,(0,0))

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
    picker.rect.x = random.randint(50,950)
    picker.rect.y = random.randint(50,550)
    ritems.add(picker)
    allitems.add(picker)
for i in range(15):
    toxic = nr()
    toxic.rect.x = random.randint(50,950)
    toxic.rect.y = random.randint(50,550)
    nritems.add(toxic)
    allitems.add(toxic)
BIN = bin()
allitems.add(BIN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    bg("bground.jpg")
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if BIN.rect.y > 0:
            BIN.rect.y -=10
    if keys[pygame.K_s]:
        if BIN.rect.y < 550:
            BIN.rect.y +=10
    if keys[pygame.K_a]:
        if BIN.rect.x > 0:
            BIN.rect.x -=10
    if keys[pygame.K_d]:
        if BIN.rect.x < 965:
            BIN.rect.x +=10
    items = pygame.sprite.spritecollide(BIN,ritems,True)
    itemstoxic = pygame.sprite.spritecollide(BIN,nritems,True)
    for i in items:
        score += 1
        scoretext = text.render("SCORE:"+str(score),True,"black")
    for i in itemstoxic:
        score -= 5
        scoretext = text.render("SCORE:"+str(score),True,"black")   
    screen.blit(scoretext,(420,10))
    allitems.draw(screen)
    pygame.display.update()
