import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Dogs:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
                 #  role
            pygame.draw.rect(screen, (164, 128, 189), (self.xpos, self.ypos, 200, 150))
            begin = font.render("Hunting Dogs", True, white)
            screen.blit(begin,(930,165))