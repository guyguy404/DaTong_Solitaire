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
    
    def _get_playable_cards(self) -> list[Card]:
        my_playable_cards = []
        for card in self.game.hand[self.id]:
            if card.playable:
                my_playable_cards.append(card)
        return my_playable_cards
    
class AiAgentRandom(AiAgent):
    """使用随机出牌策略的电脑玩家"""
    def __init__(self, id):
        super().__init__(id)
    
    def get_card_to_play(self) -> Card:
        return choice(self._get_playable_cards())

    def get_card_to_discard(self) -> Card:
        return choice(self.game.hand[self.id].sprites())

class AiAgentNormal(AiAgent):
    """一个正常的电脑玩家"""
    def __init__(self, id):
        super().__init__(id)
        
    def get_card_to_play(self) -> Card:
        my_playable_cards = self._get_playable_cards()
        if len(my_playable_cards) == 1:
            return my_playable_cards[0]
        card_point_list: list[list[Card, int]] = [[card, 0] for card in my_playable_cards]
        my_hand = self.game.hand[self.id]
        for card_point_pair in card_point_list:
            card = card_point_pair[0]
            for hand_card in my_hand:
                if card.rank >= 7:
                    if hand_card.suit == card.suit and hand_card.rank > card.rank:
                        card_point_pair[1] += hand_card.rank
                if card.rank <= 7:
                    if hand_card.suit == card.suit and hand_card.rank < card.rank:
                        card_point_pair[1] += hand_card.rank
        return sorted(card_point_list, key=lambda l: l[1], reverse=True)[0][0]
    
    def get_card_to_discard(self) -> Card:
        my_hand = self.game.hand[self.id]
        card_point_list: list[list[Card, int]] = [[card, card.rank] for card in my_hand]
        for card_point_pair in card_point_list:
            card = card_point_pair[0]
            for hand_card in my_hand:
                if card.rank >= 7:
                    if hand_card.suit == card.suit and hand_card.rank > card.rank:
                        card_point_pair[1] += hand_card.rank
                if card.rank <= 7:
                    if hand_card.suit == card.suit and hand_card.rank < card.rank:
                        card_point_pair[1] += hand_card.rank
        return sorted(card_point_list, key=lambda l: l[1], reverse=False)[0][0]