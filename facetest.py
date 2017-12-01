import face

import pygame,sys
from pygame.locals import *

pygame.init()
mainSurface = pygame.display.set_mode((700,700),0,32)
myface = face.Face(mainSurface)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        elif event.type == MOUSEBUTTONDOWN:
            myface.drawFace(pygame.mouse.get_pos())

    pygame.display.update()