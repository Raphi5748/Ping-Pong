import pygame
import time
import sys
import math
import random
pygame.init()
uhr = pygame.time.Clock()
spiel_Aktiv = True
vx = 2
vy = 2

BREITE = 1000
HOEHE = 600
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption('Ping_Pong')
pygame.display.flip()

background = pygame.image.load('Tennisplatz.webp')
background = pygame.transform.scale(background, (BREITE,HOEHE))


Balken = pygame.image.load('neuerbalken.png')
Balken = pygame.transform.scale(Balken, (25,200))
x = BREITE / 5
y = HOEHE / 2
Balken_rechteck = Balken.get_rect(center = (x,y))

Balken2 = pygame.image.load('neuerbalken.png')
Balken2 = pygame.transform.scale(Balken, (25,200))
x = BREITE / 5 * 4
y = HOEHE / 2
Balken2_rechteck = Balken2.get_rect(center = (x,y))

Kugel = pygame.image.load('KugelPingPong.png')
Kugel = pygame.transform.scale(Kugel, (100,100))
x = BREITE / 2
y = HOEHE / 2
Kugel_rechteck = Kugel.get_rect(center = (x,y))



while spiel_Aktiv:
   
    #ballrechteck = pygame.draw.ellipse(fenster, (255,255,0), [Kugel_rechteck.centerx - 490 ,Kugel_rechteck.centery - 493 ,110,110], 1)
    # = pygame.draw.rect(fenster, (255,255,0), [Balken_rechteck.centerx - 75, Balken_rechteck.centery - 305 , 25, 260], 1)
    #spieler2rechteck = pygame.draw.rect(fenster, (255,255,0), [Balken2_rechteck.centerx - 75, Balken2_rechteck.centery - 305 , 25, 260], 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
            pygame.quit()
            sys.exit()
    tastatur = pygame.key.get_pressed()
    
    if tastatur[pygame.K_w] == 1:
        Balken_rechteck.centery -= 5
    if tastatur[pygame.K_s] == 1:
        Balken_rechteck.centery += 5
        
    if tastatur[pygame.K_UP] == 1:
        Balken2_rechteck.centery -= 5
    if tastatur[pygame.K_DOWN] == 1:
        Balken2_rechteck.centery += 5
    
    Kugel_rechteck.centerx += vx
    Kugel_rechteck.centery += vy 
    if Kugel_rechteck.colliderect(Balken_rechteck):
        print("Zusammenstoß Balken 2 und Ball")
        vy = random.randint(-5,5)
        vx -= 1
        vx = vx * -1
        print(vx)
        betrag =  Balken_rechteck.right - Kugel_rechteck.left 
        print(betrag)
        Kugel_rechteck.centerx = Kugel_rechteck.centerx + betrag

    if Kugel_rechteck.colliderect(Balken2_rechteck): 
        print("Zusammenstoß Balken und Ball")
        vy = random.randint(-5,5)
        vx += 1
        vx = vx * -1
        print(vx)
        betrag = Kugel_rechteck.right - Balken2_rechteck.left 
        Kugel_rechteck.centerx = Kugel_rechteck.centerx - betrag
        
    if Kugel_rechteck.top < 0:
        vy = vy * -1
    
    if Kugel_rechteck.bottom > 600 :
        vy = vy * -1

    fenster.blit(background, (0,0))
    fenster.blit(Balken,Balken_rechteck)
    fenster.blit(Balken2,Balken2_rechteck)
    fenster.blit(Kugel,Kugel_rechteck)
    
  
    pygame.display.update()
    uhr.tick(120)
    



