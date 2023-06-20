import pygame
import time
import sys
import math
import random
pygame.init()
uhr = pygame.time.Clock()
Pause = False 
spiel_Aktiv = True
vx = 2
vy = 2

punktzahls1 = 0
punktzahls2 = 0

BREITE = 1000
HOEHE = 600
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption('Ping_Pong')
pygame.display.flip()

background = pygame.image.load('Tennisplatz.webp')
background = pygame.transform.scale(background, (BREITE,HOEHE))


Balken = pygame.image.load('neuerbalken.png')
Balken = pygame.transform.scale(Balken, (25,200))
x = BREITE / 6
y = HOEHE / 2
Balken_rechteck = Balken.get_rect(center = (x,y))

Balken2 = pygame.image.load('neuerbalken.png')
Balken2 = pygame.transform.scale(Balken, (25,200))
x = BREITE / 6 * 5
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
       
    if tastatur[pygame.K_ESCAPE] == 1:
        Pause = True 
        
    while Pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_aktiv = False
                pygame.quit()
                sys.exit()
            print("Pause")
            tastatur = pygame.key.get_pressed()
            if tastatur[pygame.K_SPACE] == 1:
                print("Enter")
                Pause = False
            print("Pause1")
            uhr.tick(120)
            pygame.display.update()
    Kugel_rechteck.centerx += vx
    Kugel_rechteck.centery += vy 
    if Kugel_rechteck.colliderect(Balken_rechteck):
        print("Zusammenstoß Balken 2 und Ball")
        vy = random.randint(-3,3)
        vx -= 0.25
        vx = vx * -1
        print(vx)
        betrag =  Balken_rechteck.right - Kugel_rechteck.left 
        print(betrag)
        if betrag < 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx + betrag
        if betrag > 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx - 13

    if Kugel_rechteck.colliderect(Balken2_rechteck): 
        print("Zusammenstoß Balken und Ball")
        vy = random.randint(-3,3)
        vx += 0.25
        vx = vx * -1
        print(vx)
        betrag = Kugel_rechteck.right - Balken2_rechteck.left
        print(betrag)
        if betrag < 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx - betrag
        if betrag > 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx + 13
    if Kugel_rechteck.top < 0:
        vy = vy * -1
    
    if Kugel_rechteck.bottom > 600 :
        vy = vy * -1
    
    if Kugel_rechteck.left > 1000 :
        punktzahls1 += 1
        print("Spieler1: " + str(punktzahls1))
        break
    if Kugel_rechteck.right < 0 :
        punktzahls2 += 1
        print("Spieler2: " + str(punktzahls2))
        break
    fenster.blit(background, (0,0))
    fenster.blit(Balken,Balken_rechteck)
    fenster.blit(Balken2,Balken2_rechteck)
    fenster.blit(Kugel,Kugel_rechteck)
    
  
    pygame.display.update()
    uhr.tick(120)
    

