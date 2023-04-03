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
        self.discard_pile: list[Group] = []
        self.played_cards_less_7: list[list[Card]] = [[], [], [], []]
        self.played_cards_greater_7: list[list[Card]] = [[], [], [], []]
        self.played_cards_7: list[list[Card]] = [[], [], [], []]
        
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
        
        # 状态
        self.focused_card: Card = None
        self.playable_cards: list[tuple] = [(0, 7)]   # 开局只能出梅花7
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(30)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if self.focused_card:
                        if self.focused_card.info in self.playable_cards:
                            
                            # 将此牌从手中移动到场上
                            card = self.focused_card
                            if card.rank < 7:
                                self.played_cards_less_7[card.suit].append(card)
                            elif card.rank > 7:
                                self.played_cards_greater_7[card.suit].append(card)
                            else:
                                self.played_cards_7[card.suit].append(card)
                            for hand in self.hand:
                                hand.remove(card)
                            
                            # 更新可打出牌的列表
                            self.playable_cards.remove(card.info)
                            if card.info == (0, 7):
                                for i in range(1, 4):
                                    self.playable_cards.append((i, 7))
                                self.playable_cards.append((0, 6))
                                self.playable_cards.append((0, 8))
                            elif card.rank == 7:
                                self.playable_cards.append((card.suit, 6))
                                self.playable_cards.append((card.suit, 8))
                            elif card.rank == 1 or card.rank == 13:
                                pass
                            elif card.rank < 7:
                                self.playable_cards.append((card.suit, card.rank - 1))
                            elif card.rank > 7:
                                self.playable_cards.append((card.suit, card.rank + 1))
                            else:
                                raise Exception("We met a mistake in updating playable_cards!")
                            
                        else:
                            print("不能打出此牌！")

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
        
        # 显示右侧玩家手牌
        top_margin = (Settings.screen_height
                       - (len(self.hand[1])-1) * Settings.hand_card_y_spacing
                       - Settings.hand_card_height) // 2
        for i, card in enumerate(self.hand[1]):
            card.rect.top = top_margin + i * Settings.hand_card_y_spacing
            card.rect.right = Settings.screen_width + 0.6 * Settings.hand_card_width
        
        # 显示对侧玩家的手牌
        right_margin = (Settings.screen_width
                       - (len(self.hand[2])-1) * Settings.hand_card_x_spacing
                       - Settings.hand_card_width) // 2
        for i, card in enumerate(self.hand[2]):
            card.rect.right = Settings.screen_width - (right_margin + i * Settings.hand_card_x_spacing)
            card.rect.top = 0 - 0.6 * Settings.hand_card_height
        
        # 显示左侧玩家手牌
        top_margin = (Settings.screen_height
                       - (len(self.hand[3])-1) * Settings.hand_card_y_spacing
                       - Settings.hand_card_height) // 2
        for i, card in enumerate(self.hand[3]):
            card.rect.top = top_margin + i * Settings.hand_card_y_spacing
            card.rect.left = 0 - 0.6 * Settings.hand_card_width
            
        # 显示场上卡牌
        for i in range(4):
            for j, card in enumerate(reversed(self.played_cards_greater_7[i])):
                card.rect.centerx = Settings.field_x_margin + i * Settings.field_x_spacing
                card.rect.centery = Settings.screen_height // 2 - (j+1) * Settings.field_y_spacing
                self.screen.blit(card.image, card.rect)

        for i in range(4):
            for j, card in enumerate(self.played_cards_7[i]):
                card.rect.centerx = Settings.field_x_margin + i * Settings.field_x_spacing
                card.rect.centery = Settings.screen_height // 2
                self.screen.blit(card.image, card.rect)
        
        for i in range(4):
            for j, card in enumerate(self.played_cards_less_7[i]):
                card.rect.centerx = Settings.field_x_margin + i * Settings.field_x_spacing
                card.rect.centery = Settings.screen_height // 2 + (j+1) * Settings.field_y_spacing
                self.screen.blit(card.image, card.rect)
        
        # 检测鼠标是否聚焦手牌
        self.focused_card = None
        pos = pygame.mouse.get_pos()
        for i, hand in enumerate(self.hand):
            for card in reversed(hand.sprites()):
                if card.rect.collidepoint(pos):
                    self.focused_card = card
                    if i == 0:
                        card.rect.bottom = Settings.screen_height
                    elif i == 1:
                        card.rect.right = Settings.screen_width
                    elif i == 2:
                        card.rect.top = 0
                    elif i == 3:
                        card.rect.left = 0
                    else:
                        raise Exception("Too many hand!")
                    break
        
        # 显示手牌
        for i in range(4):
            self.hand[i].draw(self.screen)


if __name__ == '__main__':
    game = DaTongSolitaire()
    game.run_game()