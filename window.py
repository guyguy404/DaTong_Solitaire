from typing import Optional
import pygame
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings

class Window(Sprite):
    """游戏中所有弹出窗口的基类"""
    def __init__(
            self,
            width: int,
            height: int,
            color=None
        ):
        self.settings = Settings()
        self.game = self.settings.game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = Surface((width, height))
        if color is None:
            self.color = self.settings.window.color
        else:
            self.color = color
        self.image.fill(self.color)
        
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def blitme(self, surface: Optional[Surface]=None) -> None:
        if surface == None:
            surface = self.screen
        surface.blit(self.image, self.rect)
    
    def update(self):
        pass