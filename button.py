import pygame
from pygame import Rect, Surface
from settings import Settings

class Button:
    
    def __init__(
            self,
            msg,
            width=200,
            height=50,
            x=None,
            y=None,
            button_color=(255, 255, 255),
            text_color=(0, 0, 0),
            font_size=20
        ):
        """初始化按钮的属性"""
        self.settings = Settings()
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.image = Surface((width, height))
        self.image.fill(button_color)
        
        # 设置按钮的尺寸和其他属性
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(self.settings.font_path, font_size)
        
        # 创建按钮的rect对象，并使其居中
        self.rect = Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        if x:
            self.rect.centerx = x
        if y:
            self.rect.centery = y
        
        # 按钮的标签只需创建一次
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.rect.width // 2, self.rect.height // 2)
    
    def blitme(self):
        button = self.image.copy()
        button.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(button, self.rect)