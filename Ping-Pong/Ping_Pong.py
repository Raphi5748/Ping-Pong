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
customicer = False
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

Bild1 = "Tennisplatz.webp"
Bild2 = "Weltraum.png"
Bild3 = "greyscreen.png"
AktivesBild = Bild1
background = pygame.image.load(AktivesBild)
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

OrangenerBallBild = "OrangenerBall.png"
PinkerBallBild = "PinkerBall.png"
TürkiserBallBild = "TürkiserBall.png"
GrünerBallBild = "GrünerBall.png"
GelberBallBild = "GelberBall.png"

AktiverBall = GrünerBallBild

Kugel = pygame.image.load(AktiverBall)
Kugel = pygame.transform.scale(Kugel, (100,100))
x = BREITE / 2
y = HOEHE / 2
Kugel_rechteck = Kugel.get_rect(center = (x,y))

OrangenerBall = pygame.image.load(OrangenerBallBild)
OrangenerBall = pygame.transform.scale(OrangenerBall, (100,100))
x = BREITE / 6
y = HOEHE / 2
OrangenerBall_rechteck = OrangenerBall.get_rect(center = (x,y))

PinkerBall = pygame.image.load(PinkerBallBild)
PinkerBall = pygame.transform.scale(PinkerBall, (100,100))
x = BREITE / 6 * 2
y = HOEHE / 2
PinkerBall_rechteck = PinkerBall.get_rect(center = (x,y))

TürkiserBall = pygame.image.load(TürkiserBallBild)
TürkiserBall = pygame.transform.scale(TürkiserBall, (100,100))
x = BREITE / 6 * 3
y = HOEHE / 2
TürkiserBall_rechteck = TürkiserBall.get_rect(center = (x,y))

GrünerBall = pygame.image.load(GrünerBallBild)
GrünerBall = pygame.transform.scale(GrünerBall, (100,100))
x = BREITE / 6 * 4
y = HOEHE / 2
GrünerBall_rechteck = GrünerBall.get_rect(center = (x,y))

GelberBall = pygame.image.load(GelberBallBild)
GelberBall = pygame.transform.scale(GelberBall, (100,100))
x = BREITE / 6 * 5
y = HOEHE / 2
GelberBall_rechteck = GelberBall.get_rect(center = (x,y))

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

Einkaufstasche = pygame.image.load('Einkaufstasche.png')
Einkaufstasche = pygame.transform.scale(Einkaufstasche, (100,100))
x = BREITE / 6 * 5
y = HOEHE / 5
Einkaufstasche_rechteck = Einkaufstasche.get_rect(center = (x,y))

Fortsetzen = pygame.image.load('Fortsetzen.png')
Fortsetzen = pygame.transform.scale(Fortsetzen, (200,100))
x = BREITE / 2
y = HOEHE / 5 * 4
Fortsetzen_rechteck = Fortsetzen.get_rect(center = (x,y))

Punktestand1 = Punktestand_Font.render(str(punktzahls1), False, (0, 0, 0))

fenster.blit(background, (0,0))
fenster.blit(Balken,Balken_rechteck)
fenster.blit(Balken2,Balken2_rechteck)
fenster.blit(Kugel,Kugel_rechteck)
fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)


#Spiel

while spiel_Aktiv:
    

    # Zeitabhänige Geschwindigkeitserhöhung
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
            
    # Initialisierung
    tastatur = pygame.key.get_pressed()
    Punktestand1 = Punktestand_Font.render(str(punktzahls1), False, (0, 0, 0))
    Punktestand2 = Punktestand_Font.render(str(punktzahls2), False, (0, 0, 0))
    SpielModusText = Punktestand_Font.render(str(AktuellerSpielModus), False, (0, 0, 0))
    
    # Steuerung
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
    # Pause Menü
    while Pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_aktiv = False
                pygame.quit()
                sys.exit()
            mp = pygame.mouse.get_pos()
            if Einkaufstasche_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                customicer = True
            while customicer == True:
                for event in pygame.event.get():
                    print(customicer)
                    if event.type == pygame.QUIT:
                        spiel_aktiv = False
                        pygame.quit()
                        sys.exit()
                        
                    fenster.blit(background, (0,0))
                    fenster.blit(OrangenerBall, OrangenerBall_rechteck)
                    fenster.blit(PinkerBall, PinkerBall_rechteck)
                    fenster.blit(TürkiserBall, TürkiserBall_rechteck)
                    fenster.blit(GrünerBall, GrünerBall_rechteck)
                    fenster.blit(GelberBall, GelberBall_rechteck)
                    fenster.blit(Fortsetzen, Fortsetzen_rechteck)
                    fenster.blit(Kugel, (BREITE / 5, HOEHE / 7))
                    uhr.tick(120)
                    pygame.display.update()
                    tastatur = pygame.key.get_pressed()
                    mp = pygame.mouse.get_pos()
                    if Fortsetzen_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                        customicer = False
                    if OrangenerBall_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                        AktiverBall = OrangenerBallBild
                    if PinkerBall_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                        AktiverBall = PinkerBallBild
                    if TürkiserBall_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                        AktiverBall = TürkiserBallBild
                    if GelberBall_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                        AktiverBall = GelberBallBild
                    if GrünerBall_rechteck.collidepoint(mp) and event.type == pygame.MOUSEBUTTONDOWN:
                        AktiverBall = GrünerBallBild
                        
                    Kugel = pygame.image.load(AktiverBall)
                    Kugel = pygame.transform.scale(Kugel, (100,100))
                    
            # Pausemenü anzeigen
            fenster.blit(background, (0,0))
            fenster.blit(PauseBild, Pause_rechteck)
            fenster.blit(Steuerung, Steuerung_rechteck)
            fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
            fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)
            # Steuerung Pausemenü
            tastatur = pygame.key.get_pressed()
            if tastatur[pygame.K_SPACE] == 1:
                pygame.mixer.music.stop()
                Pause = False
            if tastatur[pygame.K_RIGHT] == 1:
                # Einzelspieler aktivieren
                EinzelSpieler = True
                AktuellerSpielModus = "Einzelspieler"
                SpielModusText = Punktestand_Font.render(str(AktuellerSpielModus), False, (0, 0, 0))
                fenster.blit(background, (0,0))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
                fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)
            if tastatur[pygame.K_LEFT] == 1:
                # Zweispieler Aktivieren
                EinzelSpieler = False
                AktuellerSpielModus = "Zweispieler"
                SpielModusText = Punktestand_Font.render(str(AktuellerSpielModus), False, (0, 0, 0))
                
                fenster.blit(background, (0,0))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
                fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)
            if tastatur[pygame.K_1] == 1:
                AktivesBild = Bild1
                background = pygame.image.load(AktivesBild)
                background = pygame.transform.scale(background, (BREITE,HOEHE))
                fenster.blit(background, (0,0))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
                fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)
            if tastatur[pygame.K_2] == 1:
                AktivesBild = Bild2
                background = pygame.image.load(AktivesBild)
                background = pygame.transform.scale(background, (BREITE,HOEHE))
                fenster.blit(background, (0,0))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
                fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)
            if tastatur[pygame.K_3] == 1:
                AktivesBild = Bild3
                background = pygame.image.load(AktivesBild)
                background = pygame.transform.scale(background, (BREITE,HOEHE))
                fenster.blit(background, (0,0))
                fenster.blit(SpielModusText, (BREITE / 6 * 4, HOEHE / 2))
                fenster.blit(Einkaufstasche, Einkaufstasche_rechteck)
            uhr.tick(120)
            pygame.display.update()
    # X und Y bewegung 
    Kugel_rechteck.centerx += vx
    Kugel_rechteck.centery += vy
    
    # wenn der Ball die Balken berührt
    if Kugel_rechteck.colliderect(Balken_rechteck):
        # zufällige y richtung
        vy = random.randint(-3,3)
        # Ball wird umgedreht
        vx = vx * -1
        # Sound wird abgespielt
        pygame.mixer.music.load('257232__javierzumer__retro-shot-blaster.wav')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(1)
        
        
        betrag =  Balken_rechteck.right - Kugel_rechteck.left 
        if betrag < 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx + betrag
        if betrag > 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx - 13

    if Kugel_rechteck.colliderect(Balken2_rechteck):
        # zufällige y richtung 
        vy = random.randint(-3,3)
        # Ball wird umgedreht
        vx = vx * -1
        # Musik abspielen
        pygame.mixer.music.load('257232__javierzumer__retro-shot-blaster.wav')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(1)
        
        betrag = Kugel_rechteck.right - Balken2_rechteck.left
        if betrag < 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx - betrag
        if betrag > 13:
            Kugel_rechteck.centerx = Kugel_rechteck.centerx + 13
            
    # Wenn der Ball die Decke oder den Boden berührt
    if Kugel_rechteck.top < 0:
        #Y richtung wird umgedreht
        vy = vy * -1
    if Kugel_rechteck.bottom > 600 :
        # Y richtung wird umgedreht
        vy = vy * -1
    # Wenn der Ball an der Seite rausgeht
    
    if Kugel_rechteck.left > 1000 :
        # Geschwindikeit wird zurückgesetzt
        vx = 2
        
        # Ball wird in die Mitte gesetzt
        Kugel_rechteck.centerx = BREITE / 2
        Kugel_rechteck.centery = HOEHE / 2
        
        # zufällige Start richtung 
        vx = vx * random.choice(plusminus)
        
        # punktzahl spieler 1 wird erhöht
        punktzahls1 += 1
        
    if Kugel_rechteck.right < 0 :
        # Geschwindikeit wird zurückgesetzt
        vx = 2
        # Ball wird in die Mitte gesetzt 
        Kugel_rechteck.centerx = BREITE / 2
        Kugel_rechteck.centery = HOEHE / 2
        # zufällige Start richtung
        vx = vx * random.choice(plusminus)
        # Punktzahl spieler 2 wird erhöht
        punktzahls2 += 1
    
    # Objekte werden angezeigt
    fenster.blit(background, (0,0))
    fenster.blit(Balken,Balken_rechteck)
    fenster.blit(Balken2,Balken2_rechteck)
    fenster.blit(Kugel,Kugel_rechteck)
    fenster.blit(Punktestand1, (Balken_rechteck.centerx, HOEHE / 8))
    fenster.blit(Punktestand2, (Balken2_rechteck.centerx, HOEHE / 8))
    
    pygame.display.update()
    uhr.tick(120)
