# Kevin Chen
# 12/01/17
# This fuction make the pygame shape about face in a pygame window

import face
import pygame
import sys
from pygame.locals import *

pygame.init()
mainSurface = pygame.display.set_mode((700, 700), 0, 32)
myface = face.Face(mainSurface)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        elif event.type == MOUSEBUTTONDOWN:
            myface.drawFace(pygame.mouse.get_pos())

    pygame.display.update()