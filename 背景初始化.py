from sys import exit
import pygame
from pygame.locals import *

pygame.init()

# ��������
ScreenWidth = 500
ScreenHright = 720
ScreenSize = (ScreenWidth, ScreenHright)
Screen = pygame.display.set_mode(ScreenSize, 0, 32)
pygame.display.set_caption("Ly's Easy Ball Game")
# ��������
pygame.mixer.music.load('music.mid')
pygame.mixer.music.play(-1, 0.0)