import pygame, sys
import random
# Initialisierung
pygame.init()
spiel_aktiv = True
uhr = pygame.time.Clock()

# Fenster
BREITE = 600
HOEHE = 600
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption('Weihnachtsspiel')
pygame.display.flip()

# Farben
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
BLAU = (0, 0, 255)
GELB = (255, 255, 0)

#bilder
background = pygame.image.load('Christmas_Background.jpg')
background = pygame.transform.scale(background, (BREITE,HOEHE))

santa = pygame.image.load('Santa-Claus.png')
santa = pygame.transform.scale(santa, (85,96))
x = BREITE // 2
y = HOEHE - 80
santa_rectangle =santa.get_rect(center=(x,y))

gift = pygame.image.load('Geschenk_01.png')
gift = pygame.transform.scale(gift, (50,50))
gift_list = []

#ereignis
erzeuge_gift = pygame.USEREVENT
pygame.time.set_timer(erzeuge_gift, 1000)


# Spielschleife (game loop)
while spiel_aktiv:
    # Ereignisse (events) bearbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
        if event.type == erzeuge_gift:
            new_gift = gift.get_rect(center=(random.randint(50,BREITE-50),50))
            gift_list.append(new_gift)
            
    tastatur = pygame.key.get_pressed()
    
    if tastatur[pygame.K_LEFT] == 1:
        santa_rectangle.centerx -= 1
    if tastatur[pygame.K_RIGHT] == 1:
        santa_rectangle.centerx += 1
    
    fenster.blit(background, (0,0))
    
    fenster.blit(santa, santa_rectangle)
    
    for g in gift_list:
        fenster.blit(gift, g)
    
    pygame.display.update()
    uhr.tick(120)

# Spielende
pygame.quit()
sys.exit()
  
             
