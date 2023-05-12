import pygame
import time
import sys
pygame.init()
uhr = pygame.time.Clock()
spiel_Aktiv = True


BREITE = 1500
HOEHE = 1000
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption('Ping_Pong')
pygame.display.flip()

Balken = pygame.image.load('pingpongbalken.png')
Balken = pygame.transform.scale(Balken, (1000,1500))
x = BREITE // 4
y = HOEHE - 80
Balken_rechteck = Balken.get_rect(center = (x,y))

while spiel_Aktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
            pygame.quit()
            sys.exit()

    fenster.blit(Balken,Balken_rechteck)
    pygame.display.update()
    uhr.tick(120)
    

  
             
