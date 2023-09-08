import pygame
import random
from pygame.locals import *


# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Se carga el archivo de la clase Cubo
import sys
sys.path.append('..')
from Cubo2 import Cubo
#from Plataforma import Cubo

#from Basura import Esfera #La esfera

from Basura import Basura
#from Plano import Plano

done = False

screen_width = 500
screen_height = 500

textures = []
front = "Front.jpg"
front2 = "Front2.jpg"
body = "Body.jpg"
side = "Side.jpg"
piso = "textura.bmp"
plata = "Platform.jpg"
texture1 = "slyth.bmp"
texture2 = "textura.bmp"
#vc para el obser.
FOVY=60.0
ZNEAR=0.01
ZFAR=900.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X=300.0
EYE_Y=200.0
EYE_Z=300.0
CENTER_X=0
CENTER_Y=0
CENTER_Z=0
UP_X=0
UP_Y=1
UP_Z=0
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500
#Dimension del plano
DimBoard = 200
DimBoard2 = 100


pygame.init()


######
#instancia plano (No se uso), No se uso Clase Plano
plan = []

#plano = Plano(dim=100)
#plan.append(plano)




def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Texturas(filepath):
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image,"RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)
    
def Init():
    global cubos, basura
    #plano  #variables

    
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: cubos")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    Texturas(piso)
    Texturas(front)
    Texturas(front2)
    Texturas(body)
    Texturas(side)  
    Texturas(plata) 
    Texturas(texture1)
    Texturas(texture2) 
    #Crear basura y cubos
    basura = [Basura(DimBoard) for i in range(80)]  #basuras
    cubos = [Cubo(DimBoard, 2.0) for i in range(5)]  #cubos, segundo argumento velocida
    
    #basuras en plano
    basura_plano = [] 
   

    
    

    ####definir objetivos
    for cubo in cubos:
        objetivo = random.choice(basura)
        while objetivo == cubo.objetivo:
            objetivo = random.choice(basura)
        cubo.objetivo = objetivo
        
        
def PlanoTexturizado():
    glColor3f(1.0,1.0,1.0)
    glEnable(GL_TEXTURE_2D)
    #Front face
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
def Plano2Texturizado():
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    # Front face
    glBindTexture(GL_TEXTURE_2D, 0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimBoard2 / 2, 0, -DimBoard2 / 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-DimBoard2 / 2, 0, DimBoard2 / 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard2 / 2, 0, DimBoard2 / 2)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(DimBoard2 / 2, 0, -DimBoard2 / 2)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    PlanoTexturizado()
    
    plano2 = Plano2Texturizado()
    
    #plano.draw()



    #for trash in basura:
        #trash.draw()
    

            
    for trash in basura:
        if not trash.pickedup:
            trash.draw()  
        
    
    for cubo in cubos:
        if (-DimBoard2 / 4 <= cubo.Position[0] <= DimBoard2 / 4) and (-DimBoard2 / 4 <= cubo.Position[2] <= DimBoard2 / 4):
            #print("Cubo tocando plano")
            if cubo.carrying_basura:
                print("Dejando basura en el plano")
                #basura.append(cubo.carrying_basura)
                delete = cubo.carrying_basura
                basura[basura.index(delete)].pickedup = True
                cubo.carrying_basura = None
                cubo.encontrar_nuevo(basura)
        cubo.mover()
        cubo.update()
        cubo.recoger_basura(basura)
        #cubo.dejar_basura(plano)

        
         # Intenta dejar la basura en el plano si la está llevando
      
        cubo.draw(textures, 0)

        

            
        




Init()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()