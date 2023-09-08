import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Basura import Basura

import random
import math

class Cubo:
    
    def __init__(self, dim, velocidad):
        
        ###########OP
        #Estados
        self.objetivo = None 
        self.recolectando = False #No se uso
        self.carrying_basura = None
  

        
        #Se inicializan las coordenadas de los vertices del cubo
        self.vertexCoords = [  
                   1,1,1,   1,1,-1,   1,-1,-1,   1,-1,1,
                  -1,1,1,  -1,1,-1,  -1,-1,-1,  -1,-1,1  ]
        #Se inicializan los colores de los vertices del cubo
        self.vertexColors = [ 
                   1,1,1,   1,0,0,   1,1,0,   0,1,0,
                   0,0,1,   1,0,1,   0,0,0,   0,1,1  ]
        #Se inicializa el arreglo para la indexación de los vertices
        self.elementArray = [ 
                  0,1,2,3, 0,3,7,4, 0,4,5,1,
                  6,2,1,5, 6,5,4,7, 6,7,3,2  ]
        
        self.DimBoard = dim
        
        #Se inicializa una posición aleatoria en el tablero
        self.Position = [0,0,0]
        
        #Inicializar las coordenadas (x, y, z) del cubo en el tablero almacenándolas en el vector Position
        self.Position[0] = random.randrange(-self.DimBoard, self.DimBoard)
        self.Position[1] = 5
        self.Position[2] = random.randrange(-self.DimBoard, self.DimBoard)

        
        #Se inicializa un vector de dirección aleatorio
        self.Direction = [0,0,0]
        
        #El vector aleatorio debe estar sobre el plano XZ (la altura en Y debe ser fija)
        #Se normaliza el vector de dirección
        self.Direction[0] = random.randrange(-200, 200)
        self.Direction[1] = 0
        self.Direction[2] = random.randrange(-200, 200)

        #Se normaliza el vector de dirección
        m = math.sqrt((self.Direction[0] * self.Direction[0]) + (self.Direction[2] * self.Direction[2])) 
        self.Direction[0] = self.Direction[0] / m
        self.Direction[2] = self.Direction[2] / m
        
        #Se cambia la magnitud del vector dirección con la variable vel
        self.velocidad = velocidad

    def update(self):
        #Se debe calcular la posible nueva posición del cubo a partir de su
        #posición actual (Position) y el vector de dirección (Direction)
        
        posx = self.Position[0]
        dirx = self.Direction[0]
        
        posz = self.Position[2]
        dirz = self.Direction[2]
        
        
        new_x = posx + dirx
        new_z = posz + dirz

        #Se debe verificar que el objeto cubo, con su nueva posible dirección
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
        
    def mover(self):
        if not self.carrying_basura and self.objetivo:  
            objetivo_pos = self.objetivo.Position ##Se obtiene la posicion del objetivo
            direccion = [objetivo_pos[0] - self.Position[0], 0, objetivo_pos[2] - self.Position[2]]
            distancia = math.sqrt(pow(direccion[0],2) + pow(direccion[2],2))

            if distancia > 0: #Evitamos divisiones en 0 cuando ya se llegue al objetivo
                direccion[0] /= distancia
                direccion[2] /= distancia

            #Se llega al objetivo
            if distancia < 5: 
                self.is_moving = False  #Detiene
            else:
                self.Position[0] += direccion[0] * self.velocidad
                self.Position[2] += direccion[2] * self.velocidad #Se actualizan las posiciones mientras sea mayor a 5 

        
 
    def recoger_basura(self, basura, plano=None):
    
        if not self.carrying_basura and self.objetivo:
            objetivo_pos = self.objetivo.Position
            distancia = math.sqrt((objetivo_pos[0] - self.Position[0])**2 + (objetivo_pos[2] - self.Position[2])**2)
            #print("Cubo recogiendo basura:", self.carrying_basura)
            #print("Objetivo antes de recoger basura:", self.objetivo)
            #print("Distancia a la basura:", distancia)
     
        
            if distancia < 5: #Cerca de basura
                

                self.carrying_basura = self.objetivo  #El cubo recoge la basura
                self.objetivo = None
                
                
                #if plano:
                   # plano.agregar_basura(self.carrying_basura) 
                   #No se puedo implementar la clase piano correctamente
              
                 

        
                        
    def encontrar_nuevo(self, basuras_disponibles):
        if not self.objetivo: 
            objetivo = random.choice(basuras_disponibles)
            self.objetivo = objetivo
            
 

    def draw(self, textures, id):    
            
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(5, 5, 5)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[id])
        
        glBegin(GL_QUADS)
        
        glColor3f(0.0, 0.8, 0.0)
        ###----- Chasis (base) -----###
        # Upper face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.5, 0.4,-1.0) # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.5, 0.4,-1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.5, 0.4, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.5, 0.4, 1.0)
        
        # Lower face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.5,-1.0, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.5,-1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.5,-1.0,-1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f( 1.5,-1.0,-1.0)
        
        # Front face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.5, 0.4, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.5, 0.4, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.5,-1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f( 1.5,-1.0, 1.0)
        
        # Back face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.5,-1.0,-1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.5,-1.0,-1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.5, 0.4,-1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.5, 0.4,-1.0)
        
        # # Left face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.5, 0.4, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.5, 0.4,-1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.5,-1.0,-1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.5,-1.0, 1.0)
        
        # Right face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.5, 0.4,-1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.5, 0.4, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.5,-1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.5,-1.0,-1.0)

        
        
        glEnd()
        glDisable(GL_TEXTURE_2D)
        
      
            
        
           
        if self.carrying_basura:
            #Mover basura
            self.carrying_basura.Position[0] = self.Position[0]
            self.carrying_basura.Position[2] = self.Position[2]

        glPopMatrix()
        
        