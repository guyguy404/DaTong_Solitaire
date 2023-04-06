import pygame
from pygame.sprite import Sprite
from pygame import Surface
from pygame.rect import Rect
from settings import Settings

class Board(Sprite):
    """管理用于显示信息的面板的类"""
    
    def __init__(self, game):
        super().__init__()
        # 暂时采用纯色背景
        self.game = game
        self.screen = pygame.display.get_surface()
        self.image = Surface((Settings.board_width, Settings.board_height))
        self.image.fill(Settings.board_color)
        self.rect = self.image.get_rect(
            x=Settings.board_x_margin,
            y=Settings.board_y_margin
        )
        self.font = pygame.font.Font(Settings.font_path, Settings.board_font_size)
        
        self.curr_player_text = self.font.render(
            "当前玩家：0",
            True,
            (10, 10, 10)
        )
        self.curr_player_text_rect = self.curr_player_text.get_rect(
            x=Settings.board_text_left_margin,
            y=Settings.board_text_top_margin
        )
        
        self.score_prompt_text = self.font.render(
            "分数：",
            True,
            (10, 10, 10)
        )
        self.score_prompt_text_rect = self.score_prompt_text.get_rect(
            x=Settings.board_text_left_margin,
            y=self.curr_player_text_rect.bottom + Settings.board_text_line_spacing
        )
        
        self.score_text:list[Surface] = []
        self.score_text_rect:list[Rect] = []
    
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
        
        self.score_text = []
        self.score_text_rect = []
        for i in range(4):
            self.score_text.append(self.font.render(
                "玩家" + str(i) + "：" + str(self.game.score[i]),
                True,
                (10, 10, 10)
            ))
            self.score_text_rect.append(self.score_text[i].get_rect(
                x=Settings.board_text_left_margin,
                y=self.score_prompt_text_rect.bottom + Settings.board_text_line_spacing + 
                    i * (Settings.board_text_line_spacing + self.score_text[i].get_rect().height)
            ))
    
    def blitme(self):
        board = self.image.copy()
        board.blit(self.curr_player_text, self.curr_player_text_rect)
        board.blit(self.score_prompt_text, self.score_prompt_text_rect)
        for i in range(4):
            board.blit(self.score_text[i], self.score_text_rect[i])
        rect = self.rect
        self.screen.blit(board, rect)