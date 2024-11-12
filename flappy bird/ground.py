import pygame
import random
pygame.init()
screen =  pygame.display.set_mode((830,850))
background = pygame.image.load("bg.png")
ground = pygame.image.load("ground.png")
flying = False
bgmove = 0
gameover = False
pipe_gap = random.randint(250, 300)
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bird.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0

    def update(self):
        if flying == True:
            self.velocity = 0 - 1

class Pipe(pygame.sprite.Sprite):
    def __init__(self,pos,x,y):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y - int(pipe_gap/2)]
        elif pos == -1:
            self.rect.topleft = [x,y + int(pipe_gap/2)]
        

flappy = Bird(300,300)

bird_group = pygame.sprite.Group()
bird_group.add(flappy)


pipe_group = pygame.sprite.Group()


while True:
    screen.blit(background,(0,0))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    screen.blit(ground,(bgmove,700))
    if flying == True and gameover == False:
        timenow = pygame.time.get_ticks()
        if timenow - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            pipebottom = Pipe(-1,700,pipe_height)
            pipetop = Pipe(1,700,pipe_height)
            pipe_group.add(pipebottom)
            pipe_group.add(pipetop)
            last_pipe = timenow
    if bgmove < -70:
        bgmove = 0
    bgmove=bgmove-0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flying= True
    bird_group.update()
    pygame.display.update()
