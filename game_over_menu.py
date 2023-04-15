import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite
from settings import Settings
from button import Button

class GameOverMenu(Sprite):
    """游戏结束时显示的菜单"""
    def __init__(self, game, sorted_player_points_pairs, score_multiply_power):
        super().__init__()
        self.game = game
        self.settings = Settings()
        self.screen = pygame.display.get_surface()
        self.image = Surface((self.settings.game_over_menu.width, self.settings.game_over_menu.height))
        self.image.fill(self.settings.game_over_menu.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.title_font = pygame.font.Font(self.settings.font_path, self.settings.game_over_menu.title.font_size)
        self.content_font = pygame.font.Font(self.settings.font_path, self.settings.game_over_menu.content.font_size)
        self.winner = sorted_player_points_pairs[0][0]
        if score_multiply_power == 2:
            self.datong = True
            self.datong_icon_image = pygame.transform.scale_by(
                pygame.image.load('images/emphasize_icon.png'),
                self.settings.game_over_menu.datong_icon.load_scale
            )
            self.datong_icon_rect = self.datong_icon_image.get_rect(
                right=self.rect.width - self.settings.game_over_menu.datong_icon.right_margin,
                top=self.settings.game_over_menu.datong_icon.top_margin
            )
        
        self.title_text = self.title_font.render(
            self.settings.player_name[self.winner] + "胜利！",
            True,
            self.settings.game_over_menu.title.color
        )
        self.title_rect = self.title_text.get_rect(
            centerx=self.rect.width // 2,
            y=self.settings.game_over_menu.title.top_margin
        )
        
        self.content_text:list[Surface] = []
        self.content_rect:list[Rect] = []
        for i in range(4):
            player = sorted_player_points_pairs[i][0]
            point = int(sorted_player_points_pairs[i][1])
            self.content_text.append(self.content_font.render(
                f"{self.settings.player_name[player]}：{point}点 —— {(self.settings.base_score[i]*score_multiply_power):+}分 -> {self.game.score[player]:+}分",
                True,
                self.settings.game_over_menu.content.color
            ))
            self.content_rect.append(self.content_text[i].get_rect(
                centerx=self.rect.width // 2,
                y=self.settings.game_over_menu.content.top_margin 
                    + i * (self.content_text[0].get_rect().height 
                           + self.settings.game_over_menu.content.line_spacing)
            ))
        self.replay_button = Button(
            msg=self.settings.game_over_menu.replay_button.msg,
            width=self.settings.game_over_menu.replay_button.width,
            height=self.settings.game_over_menu.replay_button.height,
            x=self.settings.game_over_menu.replay_button.centerx,
            y=self.settings.game_over_menu.replay_button.centery,
            button_color=self.settings.game_over_menu.replay_button.color,
            text_color=self.settings.game_over_menu.replay_button.text_color,
            font_size=self.settings.game_over_menu.replay_button.font_size,
            parent_obj=self
        )
        self.exit_button = Button(
            msg=self.settings.game_over_menu.exit_button.msg,
            width=self.settings.game_over_menu.exit_button.width,
            height=self.settings.game_over_menu.exit_button.height,
            x=self.settings.game_over_menu.exit_button.centerx,
            y=self.settings.game_over_menu.exit_button.centery,
            button_color=self.settings.game_over_menu.exit_button.color,
            text_color=self.settings.game_over_menu.exit_button.text_color,
            font_size=self.settings.game_over_menu.exit_button.font_size,
            parent_obj=self
        )
    
    def update(self):
        pass
    
    def blitme(self):
        menu = self.image.copy()
        menu.blit(self.title_text, self.title_rect)
        for i in range(len(self.content_text)):
            menu.blit(self.content_text[i], self.content_rect[i])
        self.replay_button.blitme(menu)
        self.exit_button.blitme(menu)
        if self.datong:
            menu.blit(self.datong_icon_image, self.datong_icon_rect)
        self.screen.blit(menu, self.rect)