import pygame
from pygame import Surface
from pygame.sprite import Sprite
from settings import Settings
from utils import darken

class Card(Sprite):
    """管理卡牌的类"""
    
    back_image = None
    discarded_back_image = None
    
    def __init__(self, suit, rank, owner, *group):
        """初始化卡牌并设置其初始位置"""
        super().__init__(*group)
        self.settings = Settings()
        self.game = self.settings.game
        self.screen = pygame.display.get_surface()
        # 加载卡牌图像
        self.card_image = pygame.image.load('images/cards/' + self._card_filename(suit, rank))
        # 原始图像太大了，需要适当缩小
        self.card_image = Card._scale_card_image_and_convert(self.card_image, self.settings.card.load_card_scale)
        self.image = self.card_image
        # self.size = self.image.get_size()
        # self.size = (self.size[0] * self.settings.card.load_card_scale, self.size[1] * self.settings.card.load_card_scale)
        # self.image = pygame.transform.scale(self.image, self.size)
        # self.image = self.image.convert()
        # 获取图像对应的矩形
        self.rect = self.image.get_rect()
        self.info = (suit, rank)
        self.suit = suit
        self.rank = rank
        self.owner = owner
        self.visible = True
        self.playable = False
        if self.info == (0, 7):
            self.playable = True
        self.focused = False
        self.discarded = False
    
    def _scale_card_image_and_convert(image: Surface, scale) -> Surface:
        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pygame.transform.scale(image, size).convert()
        return image
    
    def _load_card_back_image():
        """加载卡背图像，存放于卡牌类的静态变量中，需要在程序开始时调用"""
        back_image = pygame.image.load('images/cards/card_back.png')
        settings = Settings()
        scale = settings.card.load_card_scale
        Card.back_image = Card._scale_card_image_and_convert(back_image, scale)
        Card.discarded_back_image = Card.back_image.copy()
        darken(Card.discarded_back_image)
        
        
    def to_discard_UI(self):
        """卡牌被弃置，需要改变卡牌的UI"""
        self.discarded = True
        if self.visible:
            darken(self.image)
        else:
            self.image = Card.discarded_back_image
    
    def to_visible(self):
        """使一张牌从不可见转为可见"""
        if self.visible:
            return
        self.visible = True
        self.image = self.card_image
    
    def to_invisible(self):
        """使一张牌从可见转为不可见"""
        if not self.visible:
            return
        self.visible = False
        if self.discarded:
            self.image = self.discarded_back_image
        else:
            self.image = self.back_image
    
    def blitme(self):
        """在指定位置绘制卡牌"""
        # TODO 正式版需要修改为其他玩家的可打出牌不发红光
        if self.playable and self.owner == self.game.current_player:
            frame_rect = self.rect.inflate(
                self.settings.card.playable_frame.width,
                self.settings.card.playable_frame.width
            )
            pygame.draw.rect(
                self.screen,
                self.settings.card.playable_frame.color,
                frame_rect,
                width=self.settings.card.playable_frame.width,
                border_radius=self.settings.card.playable_frame.border_radius
            )
        if self.visible:
            self.screen.blit(self.image, self.rect)
        else:
            if self.discarded:
                self.screen.blit(Card.discarded_back_image, self.rect)
            else:
                self.screen.blit(Card.back_image, self.rect)
        
        
    
    def _card_filename(self, suit, rank) -> str:
        """根据参数生成对应的卡牌图像名称"""
        rank_str = ''
        if type(suit) == int:
            suit = self.settings.card.suits[suit]
        
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
    
    def cmp(x, y):
        """返回两个卡牌的顺序关系"""
        if x[0] < y[0] or x[0] == y[0] and x[1] < y[1]:
            return -1
        elif x[0] > y[0] or x[0] == y[0] and x[1] > y[1]:
            return 1
        else:
            return 0