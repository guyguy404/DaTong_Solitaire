import sys
import pygame
from pygame.sprite import Sprite, Group
from random import shuffle
from functools import cmp_to_key

from settings import Settings
from card import Card

class DaTongSolitaire:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        Settings.screen_height = self.screen.get_rect().height
        Settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("大通纸牌")
        
        self.hand: list[Group] = []
        self.discard_pile = []
        self.played_cards = []
        
        # 手牌为一个list，里面包含4个Group，每个Group代表一个人的手牌
        for i in range(4):
            self.hand.append(Group())
        
        # 生成卡牌，洗牌并发牌
        cards = []
        for i in range(4):
            for j in range(1, 13+1):
                cards.append((i, j))
        shuffle(cards)
        for i in range(4):
            hand_cards = cards[i*13:(i+1)*13]
            hand_cards.sort(key=cmp_to_key(Card.cmp))
            for card_tuple in hand_cards:
                Card(*card_tuple, self.hand[i])
    
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(Settings.bg_color)
        self._update_hands()
        
        pygame.display.flip()
    
    def _update_hands(self):
        """更新手牌图像"""
        
        # 显示我的手牌
        left_margin = (Settings.screen_width
                       - (len(self.hand[0])-1) * Settings.hand_card_x_spacing
                       - Settings.hand_card_width) // 2
        for i, card in enumerate(self.hand[0]):
            card.rect.left = left_margin + i * Settings.hand_card_x_spacing
            card.rect.bottom = Settings.screen_height + 0.6 * Settings.hand_card_height
        self.hand[0].draw(self.screen)
        
        # 显示右侧玩家手牌
        top_margin = (Settings.screen_height
                       - (len(self.hand[1])-1) * Settings.hand_card_y_spacing
                       - Settings.hand_card_height) // 2
        for i, card in enumerate(self.hand[1]):
            card.rect.top = top_margin + i * Settings.hand_card_y_spacing
            card.rect.right = Settings.screen_width + 0.6 * Settings.hand_card_width
        self.hand[1].draw(self.screen)
        
        # 显示对侧玩家的手牌
        right_margin = (Settings.screen_width
                       - (len(self.hand[2])-1) * Settings.hand_card_x_spacing
                       - Settings.hand_card_width) // 2
        for i, card in enumerate(self.hand[2]):
            card.rect.right = Settings.screen_width - (right_margin + i * Settings.hand_card_x_spacing)
            card.rect.top = 0 - 0.6 * Settings.hand_card_height
        self.hand[2].draw(self.screen)
        
        # 显示左侧玩家手牌
        top_margin = (Settings.screen_height
                       - (len(self.hand[3])-1) * Settings.hand_card_y_spacing
                       - Settings.hand_card_height) // 2
        for i, card in enumerate(self.hand[3]):
            card.rect.top = top_margin + i * Settings.hand_card_y_spacing
            card.rect.left = 0 - 0.6 * Settings.hand_card_width
        self.hand[3].draw(self.screen)


if __name__ == '__main__':
    game = DaTongSolitaire()
    game.run_game()