import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))
clock = pygame.time.Clock()
gameover = False
state = "menu"

xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class PM_file:
    def __init__(self, xpos: int, ypos: int, name: str, color: tuple[int, int, int]):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name
        self.color = color

    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 200, 150))
            begin = font.render(self.name, True, white)
            screen.blit(begin,(self.xpos +70, self.ypos +160))

class Mori(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Mori", (161,145,188))