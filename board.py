import pygame
from pygame.sprite import Sprite
from settings import Settings

class Board(Sprite):
    """管理用于显示信息的面板的类"""
    
    def __init__(self, game):
        super().__init__()
        # 暂时采用纯色背景
        self.game = game
        self.screen = pygame.display.get_surface()
        self.image = pygame.Surface((Settings.board_width, Settings.board_height))
        self.image.fill(Settings.board_color)
        self.rect = self.image.get_rect(
            x=Settings.board_x_margin,
            y=Settings.board_y_margin
        )
        self.font = pygame.font.Font(Settings.font_path, Settings.board_font_size)
        self.curr_player_text = None
    
    def update(self):
        self.curr_player_text = self.font.render(
            "当前玩家：" + str(self.game.current_player),
            True,
            (10, 10, 10)
        )
        self.curr_player_text_rect = self.curr_player_text.get_rect(
            x=Settings.board_text_left_margin,
            y=Settings.board_text_top_margin
        )
    
    def blitme(self):
        board = self.image.copy()
        board.blit(self.curr_player_text, self.curr_player_text_rect)
        rect = self.rect
        self.screen.blit(board, rect)