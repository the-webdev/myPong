'''
Created on 31.03.2012

@author: Lisa und Jan
'''
import pygame,os
pygame.init()
class Paddle(pygame.sprite.Sprite):
    '''
    Paddle for a Pong Game
    '''


    def __init__(self,xy):
        '''
        Constructor
        '''
        self.image = pygame.image.load(os.path.join(os.getenv("HOME") or os.getenv("USERPROFILE"), "pong_paddle.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = xy
        self.ms = 5
        self.velocity = 0
    def up(self):
        self.velocity -= self.movementspeed
    def down(self):
        self.velocity += self.movementspeed
    def move(self, dy):
        """Move the paddle in the y direction. Don't go out the top or bottom"""
        if self.rect.bottom + dy > 400:
            self.rect.bottom = 400
        elif self.rect.top + dy < 0:
            self.rect.top = 0
        else:
            self.rect.y += dy
    def update(self):
        """Update the Paddle"""
        self.move(self.velocity)