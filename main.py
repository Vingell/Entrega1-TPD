import pygame, sys, random
from pygame.locals import *
import time

pygame.init()
def imagen(archivo, transparencia =False):
    try: image =  pygame.image.load(archivo)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparencia:
        color= image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption('Sprite')
sprite= imagen('yoshi.png', True)
spriteflip=pygame.transform.flip(sprite, True, False)
pasto= pygame.transform.flip(imagen('pasto.png', True), False, True)
numero=80
fondo=imagen('fondo.png', False)
pospasto={}
for i in range(numero):
    pospasto[i]=(random.randint(0,800), random.randint(0,600))
def generarpasto():
    for i in range(numero):
        pantalla.blit(pasto,pospasto[i])      

cuanto=30
tiempo=0
mirar_derecha=False
mirar_arriba=False
mirar_izquierda=False
mirar_abajo=False

fotograma=0
yoshi_abajo= {}
yoshi_abajo[0]=(9,6,15,32)
yoshi_abajo[1]=(29,6,15,32)
yoshi_abajo[2]=(49,6,15,32)
yoshi_abajo[3]=(69,6,15,32)
yoshi_abajo[4]=(89,6,15,32)
yoshi_abajo[5]=(109,6,15,32)
yoshi_abajo[6]=(129,6,15,32)
yoshi_abajo[7]=(149,6,15,32)

yoshi_arriba={}
yoshi_arriba[0]=(9,47,15,32)
yoshi_arriba[1]=(29,47,15,32)
yoshi_arriba[2]=(49,47,15,32)
yoshi_arriba[3]=(69,47,15,32)
yoshi_arriba[4]=(89,47,15,32)
yoshi_arriba[5]=(109,47,15,32)
yoshi_arriba[6]=(129,47,15,32)
yoshi_arriba[7]=(149,47,15,32)

yoshi_izquierda={}
yoshi_izquierda[0]=(9,86,24,32)
yoshi_izquierda[1]=(37,86,24,32)
yoshi_izquierda[2]=(65,86,24,32)
yoshi_izquierda[3]=(93,86,24,32)
yoshi_izquierda[4]=(121,86,24,32)
yoshi_izquierda[5]=(149,86,24,32)
yoshi_izquierda[6]=(177,86,24,32)
yoshi_izquierda[7]=(205,86,24,32)

yoshi_derecha={}
yoshi_derecha[0]=(313,86,24,32)
yoshi_derecha[1]=(285,86,24,32)
yoshi_derecha[2]=(258,86,24,32)
yoshi_derecha[3]=(230,86,24,32)
yoshi_derecha[4]=(201,86,24,32)
yoshi_derecha[5]=(173,86,24,32)
yoshi_derecha[6]=(145,86,24,32)
yoshi_derecha[7]=(118,86,24,32)

yoshi_lengua_izq={}
yoshi_lengua_izq[0]=(9,171,32,27)
yoshi_lengua_izq[1]=(46,171,35,27)
yoshi_lengua_izq[2]=(86,171,39,27)
yoshi_lengua_izq[3]=(130,171,40,27)

yoshi_lengua_der={}
yoshi_lengua_der[0]=(305,171,32,27)
yoshi_lengua_der[1]=(265,171,35,27)
yoshi_lengua_der[2]=(221,171,39,27)
yoshi_lengua_der[3]=(176,171,40,27)

posx= 200
posy= 100
pantalla.blit(fondo,(0,0)) 
generarpasto()
pantalla.blit(sprite,(posx,posy), yoshi_abajo[0])
pygame.display.update()

pygame.mixer.music.load('08 - Makarov.mp3')

pygame.mixer.music.play(-1, 34)

def mover():
    global tiempo, fotograma, posx, posy
    if left:
        if posx > 0:
            posx-=1
        pantalla.blit(sprite,(posx,posy), yoshi_izquierda[fotograma])
        generarpasto()
        pygame.display.update()
    elif right:
        if posx <800-24:
            posx+=1
        pantalla.blit(spriteflip,(posx,posy), yoshi_derecha[fotograma])
        generarpasto()
        pygame.display.update()
    elif up:
        if posy >0:
            posy-=1
        pantalla.blit(sprite,(posx,posy), yoshi_arriba[fotograma])
        generarpasto()
        pygame.display.update()
    elif down:
        if posy<600-32:
            posy+=1
        pantalla.blit(sprite,(posx,posy), yoshi_abajo[fotograma])
        generarpasto()
        pygame.display.update()
    elif lengua:
        for i in range(3):
            if mirar_izquierda:
                pantalla.blit(sprite,(posx, posy),yoshi_lengua_izq[i])
            elif mirar_derecha:
                pantalla.blit(spriteflip,(posx, posy),yoshi_lengua_der[i])
            pygame.time.delay(10)
            generarpasto()
            pygame.display.update()
            pantalla.blit(fondo,(0,0)) 
        for i in range(4):
            if mirar_izquierda:
                pantalla.blit(sprite,(posx, posy),yoshi_lengua_izq[3-i])
            elif mirar_derecha:
                pantalla.blit(spriteflip,(posx, posy),yoshi_lengua_der[3-i])
            pygame.time.delay(10)
            generarpasto()
            pygame.display.update()
            pantalla.blit(fondo,(0,0)) 
        if mirar_izquierda:
            pantalla.blit(sprite,(posx, posy),yoshi_izquierda[0])
        elif mirar_derecha:
            pantalla.blit(spriteflip,(posx, posy),yoshi_derecha[0])
        generarpasto()
        pygame.display.update()
                        
    if pygame.time.get_ticks()-tiempo>cuanto:
        tiempo=pygame.time.get_ticks()
        fotograma+=1
        if fotograma==8:
            fotograma=0

 



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    tecla= pygame.key.get_pressed()
    left=False
    right=False
    up= False
    down=False
    lengua=False
    
    if tecla[K_SPACE]:
        lengua=True
        mover()
    elif tecla[K_w]:
        mirar_arriba=True
        mirar_abajo=False
        mirar_izquierda=False
        mirar_derecha=False
        up=True
        mover()
    elif tecla[K_s]:
        mirar_arriba=False
        mirar_abajo=True
        mirar_izquierda=False
        mirar_derecha=False
        down= True
        mover()
    elif tecla[K_a]:
        mirar_arriba=False
        mirar_abajo=False
        mirar_izquierda=True
        mirar_derecha=False
        left=True
        mover()
    elif tecla[K_d]:
        mirar_arriba=False
        mirar_abajo=False
        mirar_izquierda=False
        mirar_derecha=True
        right=True
        mover()
    else:
        if mirar_izquierda:
            pantalla.blit(sprite,(posx, posy),yoshi_izquierda[0])
            generarpasto()
            pygame.display.update()
        elif mirar_derecha:
            pantalla.blit(spriteflip,(posx, posy),yoshi_derecha[0])
            generarpasto()
            pygame.display.update()
        elif mirar_abajo:
            pantalla.blit(sprite,(posx, posy),yoshi_abajo[0])
            generarpasto()
            pygame.display.update()
        elif mirar_arriba:
            pantalla.blit(sprite,(posx, posy),yoshi_arriba[0])
            generarpasto()
            pygame.display.update()
        
    pantalla.blit(fondo,(0,0)) 
    
    
    
    
