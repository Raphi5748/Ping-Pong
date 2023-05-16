import pygame
import time
import sys
pygame.init()
uhr = pygame.time.Clock()
spiel_Aktiv = True
vx = 2 

BREITE = 1000
HOEHE = 600
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption('Ping_Pong')
pygame.display.flip()

background = pygame.image.load('Tennisplatz.webp')
background = pygame.transform.scale(background, (BREITE,HOEHE))


Balken = pygame.image.load('pingpongbalken.png')
Balken = pygame.transform.scale(Balken, (1000,1000))
x = BREITE -820
y = HOEHE - 80
Balken_rechteck = Balken.get_rect(center = (x,y))

Balken2 = pygame.image.load('pingpongbalken.png')
Balken2 = pygame.transform.scale(Balken, (1000,1000))
x = BREITE -55
y = HOEHE - 80
Balken2_rechteck = Balken2.get_rect(center = (x,y))

Kugel = pygame.image.load('KugelPingPong.png')
Kugel = pygame.transform.scale(Kugel, (150,150))
x = BREITE // 1.5
y = HOEHE + 20
Kugel_rechteck = Balken.get_rect(center = (x,y))



while spiel_Aktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
            
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
    if Kugel_rechteck.colliderect(Balken2_rechteck):
        
        print("Zusammenstoß Balken und Ball")
        
    fenster.blit(background, (0,0))
    fenster.blit(Balken,Balken_rechteck)
    fenster.blit(Balken2,Balken2_rechteck)
    fenster.blit(Kugel,Kugel_rechteck)
    pygame.display.update()
    uhr.tick(120)
    
pygame.quit()
sys.exit()
             


