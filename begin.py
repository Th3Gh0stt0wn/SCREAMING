import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Begin:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (200, 250, 200), (self.xpos, self.ypos, 200, 150)) #(color,color,color), (xpos, ypos, xsize, ysize) #Random top button
            begin = font.render("Begin", True, white)
            screen.blit(begin,(75,165))