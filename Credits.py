 #credits
        #pygame.draw.rect(screen, (200, 250, 200), (900, 600, 200, 150))
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class woowo:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (96, 247, 162), (self.xpos, self.ypos, 200, 150))
            begin = font.render("Citizen", True, white)
     #       screen.blit(begin,(590,165))