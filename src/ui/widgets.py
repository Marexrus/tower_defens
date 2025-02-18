import pygame

def label(screen, text, pos, color=[255, 0, 255], size=48, f=None):
    font = pygame.font.Font(f, size)
    text_render = font.render(text, False, color)
    screen.blit(text_render, pos)


class Button:
    def __init__(self, screen, func, rect, text, text_pos=[10, 10], bg=[203, 0, 119], color=[0, 0, 0], size=48):
        self.id = 'button'
        self.screen = screen

        self.func = func
        self.rect = rect
        self.bg = bg
        self.bg0 = bg
        self.bg = self.bg0.copy()
        self.text = text
        self.color = color
        self.size = size
        self.text_pos = [self.rect.x + 10, self.rect.y + 10]
        # text_pos выставляется относительно фона кнопки
        self.text_pos = [self.rect.x + text_pos[0], self.rect.y + text_pos[1]]

        objects.append(self)

    """def draw(self):
        pygame.draw.rect(self.screen, self.rect, self.bg)
        label(self.screen, self.text, [self.rect.x, self.rect.y])"""

    def draw(self, mrect):
        self.bg = self.bg0.copy()
        if self.rect.colliderect(mrect.prect):
            self.func()

        pygame.draw.rect(self.screen, self.bg, self.rect.prect)
        label(self.screen, self.text, self.text_pos, self.color, self.size)

    """def check(self, mrect):
        # self.mrect = mrect
        if self.rect.colliderect(mrect.prect):
            self.func()"""
