from __future__ import annotations
import pygame
from singleton import Singleton
from typing import TYPE_CHECKING

# 关于如何解决 Python type hints 导致的 circular imports 的问题，详见下述链接
# https://adamj.eu/tech/2021/05/13/python-type-hints-how-to-fix-circular-imports/

if TYPE_CHECKING:
    from datong_solitaire import DaTongSolitaire

class Settings(Singleton):
    """存储游戏中所有设置的类"""
    
    has_inited = False
    
    def __init__(self, game: DaTongSolitaire=None):
        """设置类的初始化（需要在游戏开始获取屏幕大小后才能初始化）"""
        # Settings 作为单例类，只初始化一次
        if Settings.has_inited:
            return
        Settings.has_inited = True
        
        # 初始化时应当提供游戏类的实例，以便后续其他的对象通过Settings类来获取游戏类的实例
        # 这样做的主要原因是
        # 游戏主体模块导入了几乎所有的其他自定义模块，这就导致其他自定义模块导入游戏主体模块时必然导致 circular imports
        # 而Settings类则几乎没有导入其他自定义模块，可以被其他自定义模块导入并获取其全局单例
        # 另一种解决方法是在构造游戏中对象实例时传入游戏主体的实例，但那样有些麻烦，不甚优雅
        if game:
            self.game = game
        else:
            raise Exception("No game provided when initializing Settings class!")
        
        self.start_menu_music = ['music/开场音乐/Sneaky-Snitch.mp3', 'music/开场音乐/Monkeys-Spinning-Monkeys.mp3', 'music/开场音乐/Fluffing-a-Duck.mp3', 'music/开场音乐/Cipher2.mp3']
        self.ai_act_interval = 1000
        # default_screen_width, default_screen_height
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
        self.player_name = ['玩家', '电脑1', '电脑2', '电脑3']
        self.start_menu = Settings.StartMenu(self.screen_width, self.screen_height)
        self.card = Settings.Card()
        self.field = Settings.Field()
        self.board = Settings.Board()
        self.game_over_menu = Settings.GameOverMenu()
        self.window = Settings.Window()
        self.rule_window = Settings.RuleWindow()
        self.exit_window = Settings.ExitWindow()
        self.stop_game_window = Settings.StopGameWindow()
    
    class Color:
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        olivedrab = (107, 142, 35)
        burlywood = (222, 184, 135)
    
    class Window:
        """与游戏中所有窗口有关的设置类"""
        def __init__(self):
            self.color = Settings.Color.burlywood
    
    class RuleWindow:
        """规则窗口的设置类"""
        def __init__(self):
            self.settings = Settings()
            self.width = 1200 * self.settings.scale_ratio
            self.height = 800 * self.settings.scale_ratio
            self.text_color = Settings.Color.black
            self.font_size = int(28 * self.settings.scale_ratio)
            self.text = """
            《大通纸牌》是一款四人纸牌接龙游戏，
            你的目标是打出尽量多的牌，并使无法打出的牌点数总和尽量小。
            游戏使用一副去掉大小王的扑克牌进行。
            发牌后从持有黑桃7的玩家开始出牌。
            第一张牌只能出黑桃7。
            之后四名玩家轮流出牌接龙，
            每种花色向场上打出的第一张牌只能是点数为7的那张牌，
            之后则是打出与其点数相邻的牌进行接龙。
            当一名玩家无牌可出时则需要从手中选择一张牌暗扣下，
            之后不得再打出此牌。
            当所有玩家都打光手牌后，每位玩家计算其所有暗扣下的牌的点数总和，
            数值按从小到大排序，如果数值相同则先出牌的排在前面，
            点数最小的是第一名，获得6分，二三四名分别失去1、2、3分。
            如果第一名的玩家的暗扣牌点数总和为0（即没有任何暗扣牌），
            则称之为“大通”，
            这一轮所有玩家的得分和失分翻倍
            （即第一名获得12分，二三四名分别失去2、4、6分）。
            """
            self.top_margin = 50 * self.settings.scale_ratio
            self.left_margin = 50 * self.settings.scale_ratio
            self.exit_button = Settings.RuleWindow.ExitButton(self.width, self.height)
            
        class ExitButton:
            """规则窗口中的“返回”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                self.settings = Settings()
                self.width = 100 * self.settings.scale_ratio
                self.height = 60 * self.settings.scale_ratio
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = int(20 * self.settings.scale_ratio)
                self.msg = '返回'
                self.centerx = surf_width // 2
                self.centery = int(surf_height * 0.9)
    
    class ExitWindow:
        """确认退出窗口的设置类"""
        def __init__(self):
            self.settings = Settings()
            self.width = 600 * self.settings.scale_ratio
            self.height = 300 * self.settings.scale_ratio
            self.text = Settings.ExitWindow.Text(self.width, self.height)
            self.confirm_button = Settings.ExitWindow.ConfirmButton(self.width, self.height)
            self.cancel_button = Settings.ExitWindow.CancelButton(self.width, self.height)
        
        class Text:
            """退出确认窗口中文字的设置类"""
            def __init__(self, surf_width, surf_height):
                self.settings = Settings()
                self.font_size = int(32 * self.settings.scale_ratio)
                self.color = Settings.Color.black
                self.text = "你确定要退出游戏吗？"
                self.centerx = surf_width // 2
                self.centery = int(surf_height * 0.25)
        
        class Button:
            """退出确认窗口中所有按钮设置信息的基类"""
            def __init__(self):
                self.settings = Settings()
                self.width = 150 * self.settings.scale_ratio
                self.height = 80 * self.settings.scale_ratio
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = int(36 * self.settings.scale_ratio)
        
        class ConfirmButton(Button):
            """退出确认窗口中的“确定”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "确定"
                self.centerx = int(surf_width * 0.3)
                self.centery = int(surf_height * 0.7)
        
        class CancelButton(Button):
            """退出确认窗口中的“取消”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "取消"
                self.centerx = int(surf_width * 0.7)
                self.centery = int(surf_height * 0.7)
    
    class StopGameWindow:
        """暂停游戏窗口的设置类"""
        def __init__(self):
            self.settings = Settings()
            self.width = 600 * self.settings.scale_ratio
            self.height = 300 * self.settings.scale_ratio
            self.text = Settings.StopGameWindow.Text(self.width, self.height)
            self.replay_button = Settings.StopGameWindow.ReplayButton(self.width, self.height)
            self.continue_button = Settings.StopGameWindow.ContinueButton(self.width, self.height)
            self.exit_button = Settings.StopGameWindow.ExitButton(self.width, self.height)
        
        class Text:
            """游戏暂停窗口中文字的设置类"""
            def __init__(self, surf_width, surf_height):
                self.settings = Settings()
                self.font_size = int(32 * self.settings.scale_ratio)
                self.color = Settings.Color.black
                self.text = "游戏已经暂停"
                self.centerx = surf_width // 2
                self.centery = int(surf_height * 0.25)
        
        class Button:
            """游戏暂停窗口中所有按钮设置信息的基类"""
            def __init__(self):
                self.settings = Settings()
                self.width = 120 * self.settings.scale_ratio
                self.height = 80 * self.settings.scale_ratio
                self.color = Settings.Color.white
                self.text_color = Settings.Color.black
                self.font_size = int(36 * self.settings.scale_ratio)
        
        class ReplayButton(Button):
            """游戏暂停窗口中的“重来”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "重来"
                self.centerx = int(surf_width * 0.2)
                self.centery = int(surf_height * 0.7)
        
        class ContinueButton(Button):
            """游戏暂停窗口中的“继续”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "继续"
                self.centerx = int(surf_width * 0.5)
                self.centery = int(surf_height * 0.7)
        
        class ExitButton(Button):
            """游戏暂停窗口中的“退出”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "退出"
                self.centerx = int(surf_width * 0.8)
                self.centery = int(surf_height * 0.7)
    
    class StartMenu:
        """开始界面的设置类"""
        button_yspacing = 150
        def __init__(self, surf_width, surf_height):
            self.title = Settings.StartMenu.Title(surf_width, surf_height)
            self.play_button = Settings.StartMenu.PlayButton(surf_width, surf_height)
            self.rule_button = Settings.StartMenu.RuleButton(surf_width, surf_height)
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
                self.font_size = int(28 * self.settings.scale_ratio)
            
        class PlayButton(Button):
            """开始界面中的“开始游戏”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "开始游戏"
                self.centerx = surf_width // 2
                self.centery = surf_height // 2
            
        # class TestButton(Button):
        #     """开始界面中的“测试游戏”按钮设置类"""
        #     def __init__(self, surf_width, surf_height):
        #         super().__init__()
        #         self.msg = "测试游戏"
        #         self.centerx = surf_width // 2
        #         self.centery = surf_height // 2 + Settings.StartMenu.button_yspacing
        
        class RuleButton(Button):
            """开始界面中的“游戏规则”按钮设置类"""
            def __init__(self, surf_width, surf_height):
                super().__init__()
                self.msg = "游戏规则"
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
            """可打出卡牌的提示框相关的设置类"""
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
            self.stop_button = Settings.Field.StopButton()
        
        class StopButton:
            """游戏时的暂停按钮"""
            def __init__(self):
                self.settings = Settings()
                self.width = 200 * self.settings.scale_ratio
                self.height = 100 * self.settings.scale_ratio
                self.color = Settings.Color.burlywood
                self.text_color = Settings.Color.black
                self.font_size = int(32 * self.settings.scale_ratio)
                self.msg = "暂停"
                self.centerx = 1520 * self.settings.scale_ratio
                self.centery = 100 * self.settings.scale_ratio
    
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
            """信息面板上文字相关的设置"""
            def __init__(self):
                self.settings = Settings()
                self.left_margin = 20 * self.settings.scale_ratio
                self.top_margin = 20 * self.settings.scale_ratio
                self.line_spacing = 10 * self.settings.scale_ratio
                self.color = Settings.Color.black

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
            self.datong_icon = Settings.GameOverMenu.DaTongIcon()
        
        class Title:
            """游戏结束界面中标题的设置类"""
            def __init__(self):
                self.settings = Settings()
                self.font_size = int(52 * self.settings.scale_ratio)
                self.color = Settings.Color.black
                self.top_margin = 50 * self.settings.scale_ratio
        
        class DaTongIcon:
            """大通时显示的标志相关的设置类"""
            def __init__(self):
                self.settings = Settings()
                self.load_scale = 1 * self.settings.scale_ratio
                self.right_margin = 0 * self.settings.scale_ratio
                self.top_margin = 0 * self.settings.scale_ratio
                
        class Content:
            """游戏结束界面中内容文字的设置类"""
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