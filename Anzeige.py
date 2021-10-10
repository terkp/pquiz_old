# -*- coding: utf-8 -*-
#from tkinter import *
from _thread import allocate_lock

# -*- coding: UTF-8 -*-

# Pygame Modul importieren.
import pygame

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')





class App:
    def __init__(self,Buff2):

        self.main(Buff2)

    def main(self,buff2):
        global running
        # Initialisieren aller Pygame-Module und 
        # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
        pygame.init()
        global screen
        screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE)

        background = pygame.image.load("Hintergrund.jpg")#Pygame can handle other
        Rahmen = pygame.image.load("ober.gif")
        background = pygame.transform.scale(background,(1920,1080))
        backgroundRect = pygame.Rect(0,0,1920,1080)#screen.get_1920,screen.get_1080)
        #size = (1920, 1080) = background.get_size() 
        #Returns size of image as (x, y) so game screen will be as big as background

        # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
        pygame.display.set_caption("PQuiz")
        pygame.mouse.set_visible(1)
        pygame.key.set_repeat(1, 10)

        # Clock Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
        clock = pygame.time.Clock()
        
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("Cambria", 40)

        button = pygame.Rect(500,700,300,100)
        button2 = pygame.Rect(900,700,300,100)
        
        # Die Schleife, und damit unser Spiel, läuft solange running == True.
        running = True
        while running:

            # Framerate auf 30 Frames pro Sekunde beschränken.
            # Pygame wartet, falls das Programm schneller läuft.
            clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running= False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running= False
                        break
            """mouse = pygame.mouse.get_pos()
            if button.collidepoint(mouse):
                buff2.setFrageT()
            if button2.collidepoint(mouse):
                buff2.weiterT()"""
            Frage=buff2.getFrage()
            # render text
            screen.fill((255,255,255))
            screen.blit(background, backgroundRect)
            if buff2.getPunkteanzeigen():
                for i in range(len(buff2.getGruppen())):
                    if buff2.getGruppen()[i][3]: #Wenn der Spieler Aktiv ist
                        label = myfont.render(buff2.getGruppen()[i][0].rstrip() , 1, (0,0,0))
                        screen.blit(label, (500,500+ 50*i))
                    else:
                        label = myfont.render(buff2.getGruppen()[i][0] , 1, (80,80,80))
                        screen.blit(label, (500,500+ 50*i))
                    label = myfont.render(str(buff2.getGruppen()[i][2]) , 1, (0,0,0))
                    screen.blit(label, (1100,500+ 50*i))
            else:
                for i in range(len(buff2.getGruppen())):
                    if buff2.getGruppen()[i][3]: #Wenn der Spieler Aktiv ist
                        label = myfont.render(buff2.getGruppen()[i][0].rstrip() , 1, (0,0,0))
                        screen.blit(label, (50,50+ 50*i))
                        if buff2.getGruppen()[i][1] != 0: #Wenn eine Anwort gegeben ist
                            if len(Frage)>1:
                                if Frage[0]=="normal":
                                    label = myfont.render(chr(buff2.getGruppen()[i][1]+64) , 1, (0,0,0))
                                    screen.blit(label, (600,50+ 50*i))
                                if Frage[0]=="schaetzen":
                                    label = myfont.render(str(buff2.getGruppen()[i][1]) , 1, (0,0,0))
                                    screen.blit(label, (600,50+ 50*i))
                                if Frage[0]=="sortier":
                                    for j in range(4):
                                        losu = str(buff2.getGruppen()[i][1][j])
                                        losu = losu.replace("1","A")
                                        losu = losu.replace("2","B")
                                        losu = losu.replace("3","C")
                                        losu = losu.replace("4","D")
                                        label = myfont.render( losu, 1, (0,0,0))
                                        screen.blit(label, (600+j*20,50+ 50*i))
                                
                    else:
                        label = myfont.render(buff2.getGruppen()[i][0] , 1, (80,80,80))
                        screen.blit(label, (50,50+ 50*i))
                    #label = myfont.render(str(buff2.getGruppen()[i][2]) , 1, (0,0,0))
                    #screen.blit(label, (340,50+ 50*i))
                if len(Frage)>1:
                    screen.blit(Rahmen,(400,320))
                    if len(Frage[1])<45:
                        label2 = myfont.render(Frage[1] , 1, (0,0,0))
                        screen.blit(label2, (500, 380))
                    else:
                        Umbruch = Frage[1].find(" ",35)
                        label2 = myfont.render(Frage[1][:Umbruch] , 1, (0,0,0))
                        screen.blit(label2, (500, 350))
                        label3 = myfont.render(Frage[1][Umbruch:] , 1, (0,0,0))
                        screen.blit(label3, (500, 410))
                    if Frage[0]=="normal":
                        lo = int(Frage[3])-1
                        losung = Frage[2][lo]
                        if buff2.get__LoesungAnzeigen():
                            losu = str(Frage[3])
                            losu = losu.replace("1","A")
                            losu = losu.replace("2","B")
                            losu = losu.replace("3","C")
                            losu = losu.replace("4","D")
                            if len(losung)<40:
                                screen.blit(myfont.render(losu+': '+losung , 1, (0,0,0)), (750, 615))
                            else:
                                screen.blit(myfont.render(losu, 1, (0,0,0)), (750, 615))
                        for i in range(4):
                            if len(Frage[2][i])<40:
                                if (i==0 or i==2):
                                    screen.blit(myfont.render(chr(i+65)+': '+Frage[2][i] , 1, (0,0,0)), (300, 550+int(i/2)*130))
                                else:
                                    screen.blit(myfont.render(chr(i+65)+': '+Frage[2][i] , 1, (0,0,0)), (1100, 550+int(i/2)*130))
                            else:
                                Umbruch = Frage[2][i].find(" ",25)
                                if (i==0 or i==2):
                                    screen.blit(myfont.render(chr(i+65)+': '+Frage[2][i][:Umbruch] , 1, (0,0,0)), (300, 550+int(i/2)*130))
                                    screen.blit(myfont.render('    '+Frage[2][i][Umbruch:] , 1, (0,0,0)), (300, 585+int(i/2)*130))
                                else:
                                    screen.blit(myfont.render(chr(i+65)+': '+Frage[2][i][:Umbruch] , 1, (0,0,0)), (1100, 550+int(i/2)*130))
                                    screen.blit(myfont.render('    '+Frage[2][i][Umbruch:] , 1, (0,0,0)), (1100, 585+int(i/2)*130)) 
                        
                        #screen.blit(myfont.render('B: '+Frage[2][1] , 1, (0,0,0)), (1200, 500))
                        #screen.blit(myfont.render('C: '+Frage[2][2] , 1, (0,0,0)), (300, 600))
                        #screen.blit(myfont.render('D: '+Frage[2][3] , 1, (0,0,0)), (1200, 600))
                    if Frage[0]=="sortier":
                        if buff2.get__LoesungAnzeigen():
                            for i in range(4):
                                losu = str(Frage[3][i])
                                losu = losu.replace("1","A")
                                losu = losu.replace("2","B")
                                losu = losu.replace("3","C")
                                losu = losu.replace("4","D")
                                screen.blit(myfont.render(losu , 1, (0,0,0)), (750+i*25, 615))
                        screen.blit(myfont.render('A: '+Frage[2][0] , 1, (0,0,0)), (300, 550))
                        screen.blit(myfont.render('B: '+Frage[2][1] , 1, (0,0,0)), (1100, 550))
                        screen.blit(myfont.render('C: '+Frage[2][2] , 1, (0,0,0)), (300, 680))
                        screen.blit(myfont.render('D: '+Frage[2][3] , 1, (0,0,0)), (1100, 680))
                    if Frage[0]=="schaetzen":
                        if buff2.get__LoesungAnzeigen():
                            screen.blit(myfont.render(str(Frage[2]) , 1, (0,0,0)), (750, 615))
            screen.blit
            pygame.display.flip()
        pygame.quit()

