from __future__ import annotations
import pygame
from singleton import Singleton
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datong_solitaire import DaTongSolitaire

class Settings(Singleton):
    """存储游戏中所有设置的类"""
    
    has_inited = False
    
    def __init__(self, game: DaTongSolitaire=None):
        """设置类的初始化（需要在游戏开始获取屏幕大小后才能初始化）"""
        if Settings.has_inited:
            return
        Settings.has_inited = True
        
        if game:
            self.game = game
        else:
            raise Exception("No game provided when initializing Settings class!")
        
        self.ai_act_interval = 1000
        self.dft_scr_w = 1707
        self.dft_scr_h = 1067
        screen_rect = pygame.display.get_surface().get_rect()
        self.screen_width = screen_rect.width
        self.screen_height = screen_rect.height
        self.scale_ratio = (self.screen_width / self.dft_scr_w + self.screen_height / self.dft_scr_h) / 2
        self.bg_color = Settings.Color.olivedrab
        self.font_name = '霞鹜文楷'
        self.font_path = 'fonts/LXGWWenKai-Regular.ttf'
        self.base_score = [6, -1, -2, -3]
        self.start_menu = Settings.StartMenu(self.screen_width, self.screen_height)
        self.card = Settings.Card()
        self.field = Settings.Field()
        self.board = Settings.Board()
        self.game_over_menu = Settings.GameOverMenu()
    
    class Color:
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        olivedrab = (107, 142, 35)
        burlywood = (222, 184, 135)    # (205, 170, 125)
    
    class StartMenu:
        """开始界面的设置类"""
        button_yspacing = 150
        def __init__(self, surf_width, surf_height):
            self.title = Settings.StartMenu.Title(surf_width, surf_height)
            self.play_button = Settings.StartMenu.PlayButton(surf_width, surf_height)
            self.test_button = Settings.StartMenu.TestButton(surf_width, surf_height)
            self.exit_button = Settings.StartMenu.ExitButton(surf_width, surf_height)
        
        class Title:
            """开始界面标题图片的设置类"""
            def __init__(self, surf_width, surf_height):
                self.centerx = surf_width // 2
                self.centery = int(surf_height * 0.3)
            
        class Button:
            """开始界面中所有按钮设置信息的基类"""
            def __init__(self):
                self.settings = Settings()
                self.width = 200 * self.settings.scale_ratio
                self.height = 100 * self.settings.scale_ratio
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = int(32 * self.settings.scale_ratio)
            
        class PlayButton(Button):
            """开始界面中的“开始游戏”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "开始游戏"
                self.centerx = surf_width // 2
                self.centery = surf_height // 2
            
        class TestButton(Button):
            """开始界面中的“测试游戏”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "测试游戏"
                self.centerx = surf_width // 2
                self.centery = surf_height // 2 + Settings.StartMenu.button_yspacing
        
        class ExitButton(Button):
            """开始界面中的“退出游戏”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "退出游戏"
                self.centerx = surf_width // 2
                self.centery = surf_height // 2 + 2 * Settings.StartMenu.button_yspacing
            
    class Card:
        """卡牌相关的设置类"""
        def __init__(self):
            self.settings = Settings()
            self.raw_width = 500
            self.raw_height = 726
            self.load_card_scale = 0.3 * self.settings.scale_ratio
            self.width = self.load_card_scale * self.raw_width
            self.height = self.load_card_scale * self.raw_height
            self.hand_xspacing = 0.5 * self.width
            self.hand_yspacing = 0.25 * self.height
            self.suits = ['spade', 'club', 'heart', 'diamond']
            self.playable_frame = Settings.Card.PlayableFrame()
        
        class PlayableFrame:
            def __init__(self):
                self.color = Settings.Color.red
                self.width = 15
                self.border_radius = 7    # 边框圆角的半径

    class Field:
        """场地相关的设置类"""
        def __init__(self):
            screen_rect = pygame.display.get_surface().get_rect()
            self.card = Settings.Card()
            self.xspacing = screen_rect.width // 6
            self.left_margin = int(self.xspacing * 1.5)
            self.yspacing = self.card.hand_yspacing
    
    class Board:
        """信息面板相关的设置类"""
        def __init__(self):
            self.settings = Settings()
            self.width = 200 * self.settings.scale_ratio
            self.height = 250 * self.settings.scale_ratio
            self.left_margin = 90 * self.settings.scale_ratio
            self.top_margin = 20 * self.settings.scale_ratio
            self.color = Settings.Color.burlywood
            self.font_size = int(20 * self.settings.scale_ratio)
            self.text = Settings.Board.Text()
        
        class Text:
            
            def __init__(self):
                self.settings = Settings()
                self.left_margin = 20 * self.settings.scale_ratio
                self.top_margin = 20 * self.settings.scale_ratio
                self.line_spacing = 10 * self.settings.scale_ratio

    class GameOverMenu:
        """游戏结束菜单设置类"""
        def __init__(self):
            self.settings = Settings()
            self.width = 1200 * self.settings.scale_ratio
            self.height = 800 * self.settings.scale_ratio
            self.color = Settings.Color.burlywood
            self.title = Settings.GameOverMenu.Title()
            self.content = Settings.GameOverMenu.Content()
            self.replay_button = Settings.GameOverMenu.ReplayButton(self.width, self.height)
            self.exit_button = Settings.GameOverMenu.ExitButton(self.width, self.height)
        
        class Title:
            
            def __init__(self):
                self.settings = Settings()
                self.font_size = int(52 * self.settings.scale_ratio)
                self.color = Settings.Color.black
                self.top_margin = 50 * self.settings.scale_ratio
        
        class Content:
            
            def __init__(self):
                self.settings = Settings()
                self.font_size = int(40 * self.settings.scale_ratio)
                self.color = Settings.Color.black
                self.top_margin = 160 * self.settings.scale_ratio
                self.line_spacing = 20 * self.settings.scale_ratio
        
        class Button:
            """游戏结束界面中所有按钮设置信息的基类"""
            def __init__(self):
                self.settings = Settings()
                self.width = 200 * self.settings.scale_ratio
                self.height = 100 * self.settings.scale_ratio
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = int(32 * self.settings.scale_ratio)
                
        class ReplayButton(Button):
            """游戏结束界面中“再来一局”按钮的设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "再来一局"
                self.centerx = surf_width // 2
                self.centery = int(surf_height * 0.65)
            
        class ExitButton(Button):
            """游戏结束界面中“退出游戏”按钮的设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "退出游戏"
                self.centerx = surf_width // 2
                self.centery = int(surf_height * 0.85)