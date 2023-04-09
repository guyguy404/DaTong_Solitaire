import pygame
from random import choice
from settings import Settings
from card import Card

class AiAgent:
    """单人游戏中的电脑玩家的基类"""
    def __init__(self, id):
        self.settings = Settings()
        self.game = self.settings.game
        self.id = id
    
    def get_card_to_play(self) -> Card:
        pass
    
    def get_card_to_discard(self) -> Card:
        pass
    
class AiAgentRandom(AiAgent):
    """使用随机出牌策略的电脑玩家"""
    def __init__(self, id):
        super().__init__(id)
    
    def get_card_to_play(self) -> Card:
        my_playable_cards = []
        for card in self.game.hand[self.id]:
            if card.playable:
                my_playable_cards.append(card)
        return choice(my_playable_cards)

    def get_card_to_discard(self) -> Card:
        return choice(self.game.hand[self.id].sprites())