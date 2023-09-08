import pygame
import random
from pygame.locals import *
from OpenGL.GL import *

class Basura:
    def __init__(self, dim):
        self.size = 10  
        self.DimBoard = dim
        self.Position = [
            random.uniform(-self.DimBoard, self.DimBoard),
            self.size / 2, 
            random.uniform(-self.DimBoard, self.DimBoard),
        ]
        

    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        #glColor3f(1.0, 0.0, 0.0)  
        
        tamano = self.size / 2
        

        glEnable(GL_TEXTURE_2D)
        #glBindTexture(GL_TEXTURE_2D, textures[id])
        glBegin(GL_QUADS)
        
        glVertex3f(-tamano, -tamano, -tamano)    
        glVertex3f(tamano, -tamano, -tamano)
        glVertex3f(tamano, -tamano, tamano)
        glVertex3f(-tamano, -tamano, tamano)

        glVertex3f(-tamano, tamano, -tamano)
        glVertex3f(tamano, tamano, -tamano)
        glVertex3f(tamano, tamano, tamano)
        glVertex3f(-tamano, tamano, tamano)

        glVertex3f(-tamano, -tamano, -tamano)
        glVertex3f(tamano, -tamano, -tamano)
        glVertex3f(tamano, tamano, -tamano)
        glVertex3f(-tamano, tamano, -tamano)

        glVertex3f(-tamano, -tamano, tamano)
        glVertex3f(tamano, -tamano, tamano)
        glVertex3f(tamano, tamano, tamano)
        glVertex3f(-tamano, tamano, tamano)

        glVertex3f(-tamano, -tamano, -tamano)
        glVertex3f(-tamano, tamano, -tamano)
        glVertex3f(-tamano, tamano, tamano)
        glVertex3f(-tamano, -tamano, tamano)

        glVertex3f(tamano, -tamano, -tamano)
        glVertex3f(tamano, tamano, -tamano)
        glVertex3f(tamano, tamano, tamano)
        glVertex3f(tamano, -tamano, tamano)

        
        glEnd()
        
        glPopMatrix()
        #glDisable(GL_TEXTURE_2D)
