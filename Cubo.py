import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

class Cubo:
    
    def __init__(self, dim, vel):
        #Se inicializa las coordenadas de los vertices del cubo
        self.vertexCoords = [  
                   1,1,1,   1,1,-1,   1,-1,-1,   1,-1,1,
                  -1,1,1,  -1,1,-1,  -1,-1,-1,  -1,-1,1  ]
        #Se inicializa los colores de los vertices del cubo
        self.vertexColors = [ 
                   1,1,1,   1,0,0,   1,1,0,   0,1,0,
                   0,0,1,   1,0,1,   0,0,0,   0,1,1  ]
        #Se inicializa el arreglo para la indexacion de los vertices
        self.elementArray = [ 
                  0,1,2,3, 0,3,7,4, 0,4,5,1,
                  6,2,1,5, 6,5,4,7, 6,7,3,2  ]
        
        self.DimBoard = dim
        
        #Se inicializa una posicion aleatoria en el tablero
        self.Position = [0,0,0]
        
        #Inicializar las coordenadas (x,y,z) del cubo en el tablero almacenandolas en el vector Position
        self.Position[0] = random.randrange(-self.DimBoard,self.DimBoard)
        self.Position[1] = 5
        self.Position[2] = random.randrange(-self.DimBoard,self.DimBoard)

        
        #Se inicializa un vector de direccion aleatorio
        self.Direction = [0,0,0]
        
        #El vector aleatorio debe de estar sobre el plano XZ (la altura en Y debe ser fija)
        #Se normaliza el vector de direccion
        self.Direction[0] = random.randrange(-200,200)
        self.Direction[1] = 0
        self.Direction[2] = random.randrange(-200,200)

        #Se normaliza el vector de direccion
        m = math.sqrt((self.Direction[0]*self.Direction[0])+(self.Direction[2]*self.Direction[2])) 
        self.Direction[0] = self.Direction[0] / m
        self.Direction[2] = self.Direction[2] / m
        
        #Se cambia la maginitud del vector direccion con la variable vel

    def update(self):
        #Se debe de calcular la posible nueva posicion del cubo a partir de su
        #posicion acutual (Position) y el vector de direccion (Direction)
        
        posx = self.Position[0]
        dirx = self.Direction[0]
        
        posz = self.Position[2]
        dirz = self.Direction[2]
        
        
        new_x = posx + dirx
        new_z = posz + dirz

        #Se debe verificar que el objeto cubo, con su nueva posible direccion
        #no se salga del plano actual (DimBoard)
        if new_x <= self.DimBoard:
            self.Position[0] = new_x
        else:
            self.Direction[0] = self.Direction[0] * -1
            
        if new_x >= -self.DimBoard:
            self.Position[0] = new_x
        else:
            self.Direction[0] = self.Direction[0] * -1
                
        if new_z <= self.DimBoard:
            self.Position[2] = new_z
        else:
            self.Direction[2] = self.Direction[2] * -1 
            
        if new_z >= -self.DimBoard:
            self.Position[2] = new_z
        else:
            self.Direction[2] = self.Direction[2] * -1 
            
    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(5,5,5)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.vertexCoords)
        glColorPointer(3, GL_FLOAT, 0, self.vertexColors)
        glDrawElements(GL_QUADS, 24, GL_UNSIGNED_INT, self.elementArray)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)
        glPopMatrix()