import pygame
from pygame.sprite import Sprite
from settings import Settings

class Card(Sprite):
    """管理卡牌的类"""
    
    def __init__(self, suit, rank, *group):
        """初始化卡牌并设置其初始位置"""
        super().__init__(*group)
        self.screen = pygame.display.get_surface()
        # 加载卡牌图像
        self.image = pygame.image.load('images/cards/' + self._card_filename(suit, rank))
        # 原始图像太大了，需要适当缩小
        self.size = self.image.get_size()
        self.size = (self.size[0] * Settings.load_card_scale, self.size[1] * Settings.load_card_scale)
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = self.image.convert()
        # 获取图像对应的矩形
        self.rect = self.image.get_rect()
    
    def blitme(self):
        """在指定位置绘制卡牌"""
        self.screen.blit(self.image, self.rect)
        
        
    
    def _card_filename(self, suit, rank) -> str:
        """根据参数生成对应的卡牌图像名称"""
        rank_str = ''
        if type(suit) == int:
            suit = Settings.suits[suit]
        
        if rank >= 2 and rank <= 10:
            rank_str = str(rank)
        elif rank == 1:
            rank_str = 'ace'
        elif rank == 11:
            rank_str = 'jack'
        elif rank == 12:
            rank_str = 'queen'
        elif rank == 13:
            rank_str = 'king'
        
        filename = rank_str + '_of_' + suit + 's'
        if rank >= 11 and rank <= 13:
            filename += '2'
        filename += '.png'
        return filename