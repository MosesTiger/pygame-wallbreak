import pygame 
import sys 
from pygame.locals import * 

pygame.init()

screen = pygame.display.set_mode((800,600))

paddle = pygame.Rect(400,500,60,10)
ball = pygame.Rect(400,300,10,10)
ball_dx = 1
ball_dy = 1 