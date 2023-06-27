#Initialisierung
import pygame
import time
import sys
import math
import random
pygame.init()
uhr = pygame.time.Clock()
Pause = True
spiel_Aktiv = True
EinzelSpieler = False
vzähler = 1
AktuellerSpielModus = "Zweispieler"
vx = 2
vy = 2
pygame.font.init()
Punktestand_Font = pygame.font.SysFont('Comic Sans MS', 30)
punktzahls1 = 0
punktzahls2 = 0
plusminus = [-1,1]

#Musik

pygame.mixer.music.load('514154__edwardszakal__game-music.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

#Spielfeld,Bilder und Steuerungselemente

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

PauseBild = pygame.image.load('Pausezeichen.png')
PauseBild = pygame.transform.scale(PauseBild, (400,100))
x = BREITE / 2
y = HOEHE / 5
Pause_rechteck = PauseBild.get_rect(center = (x,y))

Steuerung = pygame.image.load('controls.png')
Steuerung = pygame.transform.scale(Steuerung, (750, 375))
x = BREITE / 4
y = HOEHE / 2
Steuerung_rechteck = Steuerung.get_rect(center = (x,y))

Punktestand1 = Punktestand_Font.render(str(punktzahls1), False, (0, 0, 0))

fenster.blit(background, (0,0))
fenster.blit(Balken,Balken_rechteck)
fenster.blit(Balken2,Balken2_rechteck)
fenster.blit(Kugel,Kugel_rechteck)

#Spiel

while spiel_Aktiv:
    vzähler += 1
    if vzähler == 120:
        
        if vx > 0 :
            vx += 0.5
            vzähler = 1
        if vx < 0 :
            vx -= 0.5
            vzähler = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_aktiv = False
            pygame.quit()
            sys.exit()
    tastatur = pygame.key.get_pressed()
    
    Punktestand1 = Punktestand_Font.render(str(punktzahls1), False, (0, 0, 0))
    Punktestand2 = Punktestand_Font.render(str(punktzahls2), False, (0, 0, 0))
    SpielModusText = Punktestand_Font.render(str(AktuellerSpielModus), False, (0, 0, 0))
    if tastatur[pygame.K_w] == 1:
        Balken_rechteck.centery -= 5
    if tastatur[pygame.K_s] == 1:
        Balken_rechteck.centery += 5
        
    if EinzelSpieler == False:
        if tastatur[pygame.K_UP] == 1:
            Balken2_rechteck.centery -= 5
        if tastatur[pygame.K_DOWN] == 1:
            Balken2_rechteck.centery += 5
    if EinzelSpieler == True:
        Balken2_rechteck.centery = Kugel_rechteck.centery
       
    if tastatur[pygame.K_ESCAPE] == 1:
        Pause = True
        pygame.mixer.music.load('514154__edwardszakal__game-music.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        
    while Pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_aktiv = False
                pygame.quit()
                sys.exit()
            
            fenster.blit(PauseBild, Pause_rechteck)
            fenster.blit(Steuerung, Steuerung_rechteck)
            fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))

            tastatur = pygame.key.get_pressed()
            if tastatur[pygame.K_SPACE] == 1:
                pygame.mixer.music.stop()
                Pause = False
            if tastatur[pygame.K_RIGHT] == 1:
                EinzelSpieler = True
                AktuellerSpielModus = "Einzelspieler"
                SpielModusText = Punktestand_Font.render(str(AktuellerSpielModus), False, (0, 0, 0))
                fenster.blit(background, (0,0))
                fenster.blit(Balken,Balken_rechteck)
                fenster.blit(Balken2,Balken2_rechteck)
                fenster.blit(Kugel,Kugel_rechteck)
                fenster.blit(Punktestand1, (Balken_rechteck.centerx, HOEHE / 8))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
            if tastatur[pygame.K_LEFT] == 1:
                EinzelSpieler = False
                AktuellerSpielModus = "Zweispieler"
                SpielModusText = Punktestand_Font.render(str(AktuellerSpielModus), False, (0, 0, 0))
                
                fenster.blit(background, (0,0))
                fenster.blit(Balken,Balken_rechteck)
                fenster.blit(Balken2,Balken2_rechteck)
                fenster.blit(Kugel,Kugel_rechteck)
                fenster.blit(Punktestand1, (Balken_rechteck.centerx, HOEHE / 8))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
                
            uhr.tick(120)
            pygame.display.update()
    Kugel_rechteck.centerx += vx
    Kugel_rechteck.centery += vy 
    if Kugel_rechteck.colliderect(Balken_rechteck):
        vy = random.randint(-3,3)
        vx = vx * -1
        pygame.mixer.music.load('257232__javierzumer__retro-shot-blaster.wav')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(1)
        betrag =  Balken_rechteck.right - Kugel_rechteck.left 
        if betrag < 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx + betrag
        if betrag > 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx - 13

    if Kugel_rechteck.colliderect(Balken2_rechteck): 
        vy = random.randint(-3,3)
        vx = vx * -1
        pygame.mixer.music.load('257232__javierzumer__retro-shot-blaster.wav')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(1)
        betrag = Kugel_rechteck.right - Balken2_rechteck.left
        if betrag < 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx - betrag
        if betrag > 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx + 13
    if Kugel_rechteck.top < 0:
        vy = vy * -1
    
    if Kugel_rechteck.bottom > 600 :
        vy = vy * -1
    
    if Kugel_rechteck.left > 1000 :
        vx = 2
        Kugel_rechteck.centerx = BREITE / 2
        Kugel_rechteck.centery = HOEHE / 2
        
        vx = vx * random.choice(plusminus)
        punktzahls1 += 1
        
    if Kugel_rechteck.right < 0 :
        vx = 2
        Kugel_rechteck.centerx = BREITE / 2
        Kugel_rechteck.centery = HOEHE / 2
        vx = vx * random.choice(plusminus)
        punktzahls2 += 1
        
    fenster.blit(background, (0,0))
    fenster.blit(Balken,Balken_rechteck)
    fenster.blit(Balken2,Balken2_rechteck)
    fenster.blit(Kugel,Kugel_rechteck)
    fenster.blit(Punktestand1, (Balken_rechteck.centerx, HOEHE / 8))
    fenster.blit(Punktestand2, (Balken2_rechteck.centerx, HOEHE / 8))
    pygame.display.update()
    uhr.tick(120)
