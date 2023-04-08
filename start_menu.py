import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite
from settings import Settings
from button import Button

class StartMenu(Sprite):
    """游戏开始界面"""
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.settings = Settings()
        self.screen = pygame.display.get_surface()
        self.image = self.screen
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        
        self.play_button = Button(
            msg=self.settings.start_menu.play_button.msg,
            width=self.settings.start_menu.play_button.width,
            height=self.settings.start_menu.play_button.height,
            x=self.settings.start_menu.play_button.centerx,
            y=self.settings.start_menu.play_button.centery,
            button_color=self.settings.start_menu.play_button.color,
            text_color=self.settings.start_menu.play_button.text_color,
            font_size=self.settings.start_menu.play_button.font_size
        )
        self.exit_button = Button(
            msg=self.settings.start_menu.exit_button.msg,
            width=self.settings.start_menu.exit_button.width,
            height=self.settings.start_menu.exit_button.height,
            x=self.settings.start_menu.exit_button.centerx,
            y=self.settings.start_menu.exit_button.centery,
            button_color=self.settings.start_menu.exit_button.color,
            text_color=self.settings.start_menu.exit_button.text_color,
            font_size=self.settings.start_menu.exit_button.font_size
        )
    
    def update(self):
        pass
    
    def blitme(self):
        menu = self.image.copy()
        self.play_button.blitme(menu)
        self.exit_button.blitme(menu)
        self.screen.blit(menu, self.rect)