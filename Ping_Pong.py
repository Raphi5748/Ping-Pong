import pygame
import time
pygame.init()
uhr = pygame.time.Clock()

spiel_Aktiv = True
BREITE = 600
HOEHE = 600 
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.flip()
while spiel_Aktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
    pygame.display.update()
    
pygame.quit()
sys.exit()
  
             