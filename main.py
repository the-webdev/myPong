# coding: UTF-8
import pygame
import Paddle
screen = pygame.display.set_mode((800,400))
pygame.init()
myPaddle = Paddle.Paddle((60,60))
done = False
true = True
clock = pygame.time.Clock()
while not done:
    myPaddle.update()
    screen.fill((255,255,255))
    screen.blit(myPaddle, myPaddle.rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    pygame.display.flip()