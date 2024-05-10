import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Security:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (196, 81, 138), (self.xpos, self.ypos, 200, 150))
            begin = font.render("Supernatural Armed Security Force", True, white)
     #       screen.blit(begin,(590,165))