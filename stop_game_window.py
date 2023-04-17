from typing import Optional
import pygame
import ptext
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings
from window import Window
from button import Button

class StopGameWindow(Window):
    """用于游戏暂停的窗口"""
    def __init__(self):
        self.settings = Settings()
        super().__init__(
            width=self.settings.stop_game_window.width,
            height=self.settings.stop_game_window.height
        )
        self.replay_button = Button(
            msg=self.settings.stop_game_window.replay_button.msg,
            width=self.settings.stop_game_window.replay_button.width,
            height=self.settings.stop_game_window.replay_button.height,
            x=self.settings.stop_game_window.replay_button.centerx,
            y=self.settings.stop_game_window.replay_button.centery,
            font_size=self.settings.stop_game_window.replay_button.font_size,
            parent_obj=self
        )
        self.continue_button = Button(
            msg=self.settings.stop_game_window.continue_button.msg,
            width=self.settings.stop_game_window.continue_button.width,
            height=self.settings.stop_game_window.continue_button.height,
            x=self.settings.stop_game_window.continue_button.centerx,
            y=self.settings.stop_game_window.continue_button.centery,
            font_size=self.settings.stop_game_window.continue_button.font_size,
            parent_obj=self
        )
        self.exit_button = Button(
            msg=self.settings.stop_game_window.exit_button.msg,
            width=self.settings.stop_game_window.exit_button.width,
            height=self.settings.stop_game_window.exit_button.height,
            x=self.settings.stop_game_window.exit_button.centerx,
            y=self.settings.stop_game_window.exit_button.centery,
            font_size=self.settings.stop_game_window.exit_button.font_size,
            parent_obj=self
        )
    
    def blitme(self, surface: Optional[Surface] = None) -> None:
        super().blitme(surface)
        ptext.draw(
            text=self.settings.stop_game_window.text.text,
            centerx=self.rect.x + self.settings.stop_game_window.text.centerx,
            centery=self.rect.y + self.settings.stop_game_window.text.centery,
            fontname=self.settings.font_path,
            fontsize=self.settings.stop_game_window.text.font_size,
            color=self.settings.stop_game_window.text.color
        )
        self.replay_button.blitme(surface=self.image)
        self.continue_button.blitme(surface=self.image)
        self.exit_button.blitme(surface=self.image)
        