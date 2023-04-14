from typing import Optional
import pygame
import ptext
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings
from window import Window
from button import Button

class RuleWindow(Window):
    """用于显示规则的窗口"""
    def __init__(self):
        self.settings = Settings()
        super().__init__(
            width=self.settings.rule_window.width,
            height=self.settings.rule_window.height
        )
        self.text = self.settings.rule_window.text
        self.exit_button = Button(
            msg="返回",
            width=100,
            height=60,
            x=self.screen_rect.centerx,
            y=self.screen_rect.centery + 300
        )
    
    def blitme(self, surface: Optional[Surface] = None) -> None:
        super().blitme(surface)
        ptext.draw(
            text=self.text,
            pos=(self.rect.x + self.settings.rule_window.left_margin, self.rect.y + self.settings.rule_window.top_margin),
            width=self.width - self.settings.rule_window.left_margin * 2,
            fontname=self.settings.font_path,
            fontsize=self.settings.rule_window.font_size,
            color=self.settings.rule_window.text_color
        )
        self.exit_button.blitme()
        