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
        
        self.title = pygame.image.load('images/title.png')
        self.title_rect = self.title.get_rect(
            centerx=self.settings.start_menu.title.centerx,
            centery=self.settings.start_menu.title.centery
        )
        
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
        self.test_button = Button(
            msg=self.settings.start_menu.test_button.msg,
            width=self.settings.start_menu.test_button.width,
            height=self.settings.start_menu.test_button.height,
            x=self.settings.start_menu.test_button.centerx,
            y=self.settings.start_menu.test_button.centery,
            button_color=self.settings.start_menu.test_button.color,
            text_color=self.settings.start_menu.test_button.text_color,
            font_size=self.settings.start_menu.test_button.font_size
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
        menu.blit(self.title, self.title_rect)
        self.play_button.blitme(menu)
        self.test_button.blitme(menu)
        self.exit_button.blitme(menu)
        self.screen.blit(menu, self.rect)