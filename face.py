# Kevin Chen
# 12/01/17
# This file set a class to draw a face

import pygame


class Face(object):
    def __init__(self, surface):
        """
        This program can set a surface for face
        :param surface:
        """
        self.surface = surface

    def drawFace(self, position):
        """
        This program for drawing face
        :param position: none
        :return:
        """
        x = position[0]
        y = position[1]
        pygame.draw.circle(self.surface, (255, 0, 0), (position), 50, 0)
        pygame.draw.circle(self.surface, (0, 0, 255), (x-25, y-18), 10, 0)
        pygame.draw.circle(self.surface, (0, 255, 0), (x+25, y-18), 10, 0)
        pygame.draw.polygon(self.surface, (255, 255, 255), ((x, y-5), (x+10, y+11), (x-10, y+11)), 0)
        pygame.draw.polygon(self.surface, (0, 0, 255), ((x+20, y+20), (x+20, y+30), (x-20, y+30), (x-20, y+20)))

