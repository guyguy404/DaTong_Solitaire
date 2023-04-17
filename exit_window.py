from typing import Optional
import pygame
import ptext
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings
from window import Window
from button import Button

class ExitWindow(Window):
    """用于确认退出的窗口"""
    def __init__(self):
        self.settings = Settings()
        super().__init__(
            width=self.settings.exit_window.width,
            height=self.settings.exit_window.height
        )
        self.confirm_button = Button(
            msg=self.settings.exit_window.confirm_button.msg,
            width=self.settings.exit_window.confirm_button.width,
            height=self.settings.exit_window.confirm_button.height,
            x=self.settings.exit_window.confirm_button.centerx,
            y=self.settings.exit_window.confirm_button.centery,
            font_size=self.settings.exit_window.confirm_button.font_size,
            parent_obj=self
        )
        self.cancel_button = Button(
            msg=self.settings.exit_window.cancel_button.msg,
            width=self.settings.exit_window.cancel_button.width,
            height=self.settings.exit_window.cancel_button.height,
            x=self.settings.exit_window.cancel_button.centerx,
            y=self.settings.exit_window.cancel_button.centery,
            font_size=self.settings.exit_window.cancel_button.font_size,
            parent_obj=self
        )
    
    def blitme(self, surface: Optional[Surface] = None) -> None:
        super().blitme(surface)
        ptext.draw(
            text=self.settings.exit_window.text.text,
            centerx=self.rect.x + self.settings.exit_window.text.centerx,
            centery=self.rect.y + self.settings.exit_window.text.centery,
            fontname=self.settings.font_path,
            fontsize=self.settings.exit_window.text.font_size,
            color=self.settings.exit_window.text.color
        )
        self.confirm_button.blitme(surface=self.image)
        self.cancel_button.blitme(surface=self.image)
        