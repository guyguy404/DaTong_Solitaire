import pygame
from singleton import Singleton

class Settings(Singleton):
    """存储游戏中所有设置的类"""
    
    def __init__(self):
        """设置类的初始化（需要在游戏开始获取屏幕大小后才能初始化）"""
        screen_rect = pygame.display.get_surface().get_rect()
        self.screen_width = screen_rect.width
        self.screen_height = screen_rect.height
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
            self.play_button = Settings.StartMenu.PlayButton(surf_width, surf_height)
            self.exit_button = Settings.StartMenu.ExitButton(surf_width, surf_height)
            
        class Button:
            """开始界面中所有按钮设置信息的基类"""
            def __init__(self):
                self.width = 200
                self.height = 100
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = 32
            
        class PlayButton(Button):
            """开始界面中的“开始游戏”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "开始游戏"
                self.centerx = surf_width // 2
                self.centery = surf_height // 2
            
        class ExitButton(Button):
            """开始界面中的“退出游戏”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "退出游戏"
                self.centerx = surf_width // 2
                self.centery = surf_height // 2 + Settings.StartMenu.button_yspacing
            
    class Card:
        """卡牌相关的设置类"""
        def __init__(self):
            self.raw_width = 500
            self.raw_height = 726
            self.load_card_scale = 0.3
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
            self.width = 200
            self.height = 250
            self.left_margin = 90
            self.top_margin = 20
            self.color = Settings.Color.burlywood
            self.font_size = 20
            self.text = Settings.Board.Text()
        
        class Text:
            
            def __init__(self):
                self.left_margin = 20
                self.top_margin = 20
                self.line_spacing = 10

    class GameOverMenu:
        """游戏结束菜单设置类"""
        def __init__(self):
            self.width = 1200
            self.height = 800
            self.color = Settings.Color.burlywood
            self.title = Settings.GameOverMenu.Title()
            self.content = Settings.GameOverMenu.Content()
            self.replay_button = Settings.GameOverMenu.ReplayButton(self.width, self.height)
            self.exit_button = Settings.GameOverMenu.ExitButton(self.width, self.height)
        
        class Title:
            
            def __init__(self):
                self.font_size = 52
                self.color = Settings.Color.black
                self.top_margin = 50
        
        class Content:
            
            def __init__(self):
                self.font_size = 40
                self.color = Settings.Color.black
                self.top_margin = 160
                self.line_spacing = 20
        
        class Button:
            """游戏结束界面中所有按钮设置信息的基类"""
            def __init__(self):
                self.width = 200
                self.height = 100
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = 32
                
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