import pygame
import random


class playershut():

    def __init__(self):
        self.score = 0
        self.shuttle = pygame.image.load('transport.png')
        self.rect = self.shuttle.get_rect()

    def hit(self):
        self.score = self.score + 1


class alien(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = 325 + random.randint(-340,365)
        self.rect.y = 50

        self.timer = 8

    


class bullet(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos):

        super().__init__()
        self.x = xpos
        self.y = ypos


class bulletfst(bullet):

    def __init__(self,xpos,ypos):

        super(bulletfst,self).__init__(xpos,ypos)
        self.spd = 10
        self.image = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


    def move(self):

        self.rect.y = self.rect.y - self.spd

class bulletslw(bullet):

    def __init__(self,xpos,ypos):

        super().__init__(xpos,ypos)
        self.spd = 5
        self.image = pygame.image.load('bullet big.png')
        self.image = pygame.transform.scale(self.image,(130,100))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def move(self):

        self.rect.y = self.rect.y - self.spd
