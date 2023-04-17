from typing import Optional
import pygame
from pygame import Rect, Surface
from pygame.sprite import Sprite
from settings import Settings
from utils import darken

class Button(Sprite):
    
    def __init__(
            self,
            msg,
            width=200,
            height=50,
            x=None,
            y=None,
            button_color=(255, 255, 255),
            text_color=(0, 0, 0),
            font_size=20,
            parent_obj=None
        ):
        """初始化按钮的属性"""
        self.settings = Settings()
        self.game = self.settings.game
        super().__init__(self.game.buttons)
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.image = Surface((width, height))
        self.image.fill(button_color)
        self.parent_obj = parent_obj
        
        # 设置按钮的尺寸和其他属性
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(self.settings.font_path, font_size)
        self.focused = False   # 是否有光标停留
        
        # 创建按钮的rect对象，并使其居中
        self.rect = Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        if x:
            self.rect.centerx = x
        if y:
            self.rect.centery = y
        
        self.abs_rect = self.rect.copy()
        curr_obj = self
        while hasattr(curr_obj, 'parent_obj') and not curr_obj.parent_obj is None:
            self.abs_rect.x += curr_obj.parent_obj.rect.x
            self.abs_rect.y += curr_obj.parent_obj.rect.y
            curr_obj = curr_obj.parent_obj
        
        # 按钮的标签只需创建一次
        self._prep_msg(msg)
        
    def _prep_msg(self, msg) -> None:
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.rect.width // 2, self.rect.height // 2)
    
    def blitme(self, surface: Optional[Surface]=None) -> None:
        if surface == None:
            surface = self.screen
        button = self.image.copy()
        if self.focused:
            darken(button, ratio=0.8)
        button.blit(self.msg_image, self.msg_image_rect)
        surface.blit(button, self.rect)
    
    def update(self) -> None:
        if (not self.game.windows) or (not self.parent_obj is None and self.game.windows and self.game.windows[-1] == self.parent_obj):
            mouse_pos = pygame.mouse.get_pos()
            if self.abs_rect.collidepoint(mouse_pos):
                self.focused = True
            else:
                self.focused = False