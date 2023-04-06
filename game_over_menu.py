import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite
from settings import Settings

class GameOverMenu(Sprite):
    """游戏结束时显示的菜单"""
    def __init__(self, game, sorted_player_points_pairs):
        super().__init__()
        self.game = game
        self.screen = pygame.display.get_surface()
        self.image = Surface((Settings.game_over_menu_width, Settings.game_over_menu_height))
        self.image.fill(Settings.game_over_menu_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.title_font = pygame.font.Font(Settings.font_path, Settings.game_over_menu_title_font_size)
        self.content_font = pygame.font.Font(Settings.font_path, Settings.game_over_menu_content_font_size)
        self.winner = sorted_player_points_pairs[0][0]
        
        self.title_text = self.title_font.render(
            " 玩家" + str(self.winner) + "胜利！",
            True,
            Settings.game_over_menu_title_color
        )
        self.title_rect = self.title_text.get_rect(
            centerx=self.rect.width // 2,
            y=Settings.game_over_menu_title_top_margin
        )
        
        self.content_text:list[Surface] = []
        self.content_rect:list[Rect] = []
        for i in range(4):
            player = sorted_player_points_pairs[i][0]
            point = int(sorted_player_points_pairs[i][1])
            self.content_text.append(self.content_font.render(
                f"玩家{player}：{point}点 —— {Settings.base_score[i]:+}分 -> {self.game.score[player]:+}分",
                True,
                Settings.game_over_menu_content_color
            ))
            self.content_rect.append(self.content_text[i].get_rect(
                centerx=self.rect.width // 2,
                y=Settings.game_over_menu_content_top_margin + i * (self.content_text[0].get_rect().height + Settings.game_over_menu_content_line_spacing)
            ))
    
    def update(self):
        pass
    
    def blitme(self):
        menu = self.image.copy()
        menu.blit(self.title_text, self.title_rect)
        for i in range(len(self.content_text)):
            menu.blit(self.content_text[i], self.content_rect[i])
        self.screen.blit(menu, self.rect)