import pygame, sys

#Main files
from Armed_detectives_agency import detective
from begin import Begin
from Citizen import citizen
from Credits import woowo
from Decay_of_angels import Angels
from Hunting_dogs import Dogs
from Police import police
from Port_Mafia import mafia
from Rats_in_the_house_of_the_dead import Rats
from Special_divison_for_unusal_powers import Division
from Supernatural_armed_security_force import Security
from The_guild import Guild

#Files
from Agency import ADA_file
from HDogs import Hunting_dogs_file
from Mafia import PM_file
from Decay import Decay_file

#Characters
from Agency import Fukuzawa
from HDogs import Fukuchi
from Mafia import Mori
from Decay import Fyodor

#Nessicary
pygame.display.set_caption("Bungo Stray Dogs")
screen = pygame.display.set_mode((1110, 800))
clock = pygame.time.Clock()
gameover = False

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False
#Text inputs

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)
#game state variable

state = "menu"
start = False
button1 = False #go back to menu
quitGame = False #quit the game
ADA = False
Port_Mafia = False
Hunting_Dogs = False
Decay_of_the_Angel = False 

#Main files
beginning = Begin(10,10)
port = mafia(300, 10)
agency = detective(600,10)
dog = Dogs (900,10) 
angel = Angels (10, 400)
guild = Guild(300, 400)
rats = Rats(600, 400)
division = Division(900, 400)
security = Security(10, 600)
cops = police (300,600)
player = citizen(600,600)
credit = woowo (900, 600)

#Files
file1 = PM_file
file2 = ADA_file
file3 = Hunting_dogs_file
file4 = Decay_file

#Characters
mori = Mori(10,10)
fukuzawa = Fukuzawa(10,10)
fukuchi = Fukuchi(10,10)
fyodor = Fyodor(10,10)

#Game loop
while not gameover:
    clock.tick(60)
    
    #input section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = False
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
    #physics section
    #print(mousePos)#uncomment for testing
    
    #state 1: menu state!------------------------------
    if state == "menu": 
        #begin
        if mousePos[0]>10 and mousePos[0]<210 and mousePos[1]>10 and mousePos[1]<160:
            start = True
        else:
            start = False

        #mafia
        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>10 and mousePos[1]<160:
            Port_Mafia = True
        else:
            Port_Mafia = False

        #agency
        if mousePos[0]>600 and mousePos[0]<800 and mousePos[1]>10 and mousePos[1]<160:
            ADA = True
        else:
            ADA = False

        #hunting dogs
        if mousePos[0]>900 and mousePos[0]<1100 and mousePos[1]>10 and mousePos[1]<160:
            Hunting_Dogs = True
        else:
            Hunting_Dogs = False

        if mousePos[0]>10 and mousePos[0]<210 and mousePos[1]>400 and mousePos[1]<550:
            Decay_of_the_Angel = True
        else: 
            Decay_of_the_Angel = False

        #begin
        if start == True and mouseDown == True:
            print("You have chosen to start the game")
            state = "playing"

        #mafia
        elif Port_Mafia == True and mouseDown == True:
            print("You have selected the Port Mafia role")
            state = "Mafia"

        #agency
        elif ADA == True and mouseDown == True:
            print("You have selected the Armed detective agency role")
            state = "Agency"

        #hunting Dogs
        elif Hunting_Dogs == True and mouseDown == True:
            print("You have selected the Hunting dogs role")
            state = "Hunting Dogs"

        #Decay of the Angel
        elif Decay_of_the_Angel == True and mouseDown == True:
            print("You have selected the Decay of the Angel role")
            state = "Decay of the Angel"

    #state 2: playing state!---------------------------
    elif state == "playing":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

        if state == "playing" and button1 == True and mouseDown == True:
            state = "menu"
            
    elif state == "credits":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"

    elif state == "Mafia":
        if quitGame == True: #pressing quit takes you back to menu
          state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Agency":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Hunting Dogs":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Decay of the Angel":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    #render section
    screen.fill((0,0,0))
    
    #menu state-------------------------------
    if state == "menu":
        #Clear the screen
        screen.fill((0,0,0))
        #Top row
        beginning.draw()
        port.draw()
        agency.draw()
        dog.draw()
        #Middle row
        angel.draw()
        guild.draw()
        rats.draw()
        division.draw()
        #Last row
        security.draw()
        cops.draw()
        player.draw()
        credit.draw()
    
    #game state-------------------------------
    elif state == "playing":
        screen.fill((0,0,0))# Clear the screen green
        pygame.draw.rect(screen, (255, 255, 255), (100, 500, 100, 100))
        
    #Mafia state
    elif state == "Mafia":
        screen.fill((0,0,0))
        file1.draw(mori)

    #Agency state
    elif state == "Agency":
        screen.fill((0,0,0))
        file2.draw(fukuzawa)

    #Hunting dogs state
    elif state == "Hunting Dogs":
         screen.fill((0,0,0))
         file3.draw(fukuchi)

    #Decay of the Angel
    elif state == "Decay of the Angel":
         screen.fill((0,0,0))
         #file.draw()
         
    pygame.display.flip()
                
#end game loop
pygame.quit()